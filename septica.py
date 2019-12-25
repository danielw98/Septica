
import random
import sys, pygame, os
from pygame.locals import *

class Controller:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = self.screen()
        self.card_size = int(691/5),int(1056/5)
        self.clock = pygame.time.Clock()
        self.offset_x = self.width/2 - 2 * self.card_size[0]
        self.offset_y = self.height - self.card_size[1]
        s = 200
        self.rect = pygame.Rect(self.width-s,self.height-s,s,s)
        self.srect = pygame.Rect(0,self.height-s,s,s)
        self.background = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.light_green = (0,255,100)
        self.current_button = self.red
        self.table = list()
        self.table_name = list()

    def top(self):
        return self.table_name[-1]

    def screen(self):
        return pygame.display.set_mode((self.width, self.height))

    def pause(self,msec):
        self.clock.tick(msec)

    def display_hand(self,hand,marked=-1):
        curr_hand = []
        o_x, o_y = self.offset_x, self.offset_y
        for idx, card in enumerate(hand):
            curr_hand.append(card)
            img = pygame.image.load(curr_hand[-1])
            card_d = pygame.transform.scale(img, self.card_size)
            if marked == idx:
                self.screen.blit(card_d, (o_x, o_y - 30))
            else:
                self.screen.blit(card_d, (o_x, o_y))
            o_x += self.card_size[0]
        pygame.display.flip()

    def clear_table(self):
        print("Apel!")
        copy = self.table_name
        self.table = list()
        self.table_name = list()
        return copy

    def display_other(self,num=4):
        o_x = self.offset_x
        img = pygame.image.load(os.path.join("Cards","green_back.png"))
        for _ in range(num):
            card_d = pygame.transform.scale(img, self.card_size)
            self.screen.blit(card_d, (o_x, 0))
            o_x += self.card_size[0]
        pygame.display.flip()

    def set_background(self,r,g,b):
        self.screen.fill((r,g,b))

    def on_my_cards(self,mx,my):
        min_x = self.width/2 - 2*self.card_size[0]
        max_x = self.width/2 + 2*self.card_size[0]
        min_y = self.height
        max_y = self.height - self.card_size[1]
        if min_x <= mx <= max_x and min_y >= my >= max_y:
            return int((mx - min_x) // self.card_size[0])
        return -1

    def handle_event(self, mx, my):
        pos = self.on_my_cards(mx,my)
        if pos != -1: print(pos)

    def move_card(self,hand,idx=-1):
        self.set_background(0,0,0)
        self.display_hand(hand,idx)
        self.display_other(len(hand))

        if idx == -1:
           self.current_button = self.red
        else:
            self.current_button = self.green
        pygame.draw.rect(self.screen, self.current_button, self.rect)

        middle = self.width / 2 - self.card_size[0] / 2, self.height / 2 - self.card_size[1] / 2
        for c in self.table:
            self.screen.blit(c,middle)
        pygame.display.flip()

    def button_over(self,mx,my):
        min_x = self.width - 200
        max_x = self.width
        min_y = self.height
        max_y = self.height - 200
        if min_x <= mx <= max_x and min_y >= my >= max_y:
            return True
        return False


    def button_clicked(self,mx,my):
        return self.button_over(mx,my) and self.current_button == self.light_green

    def display_button(self):
        pygame.draw.rect(self.screen, self.current_button, self.rect)

    def toggle_rectangle(self,mx,my):
        if self.button_over(mx,my):
            if self.current_button == self.green:
                self.current_button = self.light_green
        elif self.current_button == self.light_green:
            self.current_button = self.green
        self.display_button()
        pygame.display.flip()

    def place_card(self,hand,idx,enemy=False):
        middle = self.width/2-self.card_size[0]/2,self.height/2-self.card_size[1]/2
        self.set_background(0, 0, 0)
        img = pygame.image.load(hand[idx])
        card = pygame.transform.scale(img, self.card_size)
        card = pygame.transform.rotate(card,random.randint(0,30))
        self.table.append(card)
        self.table_name.append(hand[idx])
        for c in self.table:
            self.screen.blit(c,middle)
        del hand[idx]
        self.current_button = self.red
        pygame.draw.rect(self.screen, self.current_button, self.rect)
        if not enemy:
            self.display_hand(hand)
            self.display_other(len(hand)+1)
        else:
            self.display_other(len(hand))


class Deck:
    def __init__(self):
        self.cards = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['S', 'H', 'C', 'D']
        self.deck = self.to_list()

    def to_list(self):
        my_list = list()
        for suit in self.suits:
            for card in self.cards:
                curr = os.path.join("Cards","%s%s.png" % (card,suit))
                my_list.append(curr)
        return my_list


class Player:
    def __init__(self,name):
        self.name = name
        self.hand = list()
        self.cards = list()
    def set_hand(self,hand):
        self.hand = hand
    def take_cards(self,cards):
        self.cards.append(cards)


def quit_conditions(event):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()

def is_winner(card, top):
    card_n = card.split('\\')[1].split('.')[0]
    top_n = top.split('\\')[1].split('.')[0]
    if card_n[:-1] == top_n[:-1] or card_n[0]=='7':
        print("OK: ",card_n, top_n)
        return True
    return False

def evaluate(hand, top):
    num = list()
    for idx, card in enumerate(hand):
        if is_winner(card,top):
            num.append(idx)
    return num


class Game:
    def __init__(self, _players):
        self.players = _players
        self.number = len(_players)
        self.deck = Deck().deck
        self.controller = Controller(1024, 768)


    def shuffle(self):
        n = random.randint(1,10)
        for i in range(n):
            random.shuffle(self.deck)

    def draw_cards(self,number):
        offset = -1-number
        hand = self.deck[-1:offset:-1]
        self.deck = self.deck[:-number]
        return hand



    def select_card(self,mx,my,hand,prev_selection):
        cardnum = self.controller.on_my_cards(mx,my)
        if cardnum == -1:
            return prev_selection

        # daca am dat click pe o carte
        # am o carte deja selectata => pun inapoi jos cartea
        if prev_selection != -1:
            self.controller.move_card(hand, -1)
            return -1

        # nu este o carte selectata anterior => o marchez drept selectata
        self.controller.move_card(hand, cardnum)
        return cardnum

    def start(self,my_turn):
        self.shuffle()
        self.controller.set_background(0,0,0)

        hand = dict()
        for i in range(self.number):
            hand[i] = self.draw_cards(4)
            self.players[i].set_hand(hand[i])

        self.controller.display_hand(hand[my_turn])
        self.controller.display_other()
        self.controller.display_button()

        turn = my_turn
        my_selection = -1
        round_ended = False
        count = 0
        first = my_turn
        winner = 0
        while 1:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                quit_conditions(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if round_ended:
                        count += 1
                        possibilities = evaluate(hand[turn],self.controller.top())
                        round_ended = False
                        if possibilities:
                            print(possibilities)
                            print(self.controller.table_name)
                            break
                        cards = self.controller.clear_table()
                        self.players[winner].take_cards(cards)
                        turn = winner
                        first = winner
                        hand[winner] += self.draw_cards(count)
                        for i in range(self.number):
                            if i is not winner:
                                hand[i] = self.draw_cards(count)
                            self.players[i].set_hand(hand[i])
                        count = 0

                    elif turn == my_turn:
                        # am ceva selectat de data trecuta si am apasat pe buton
                        if my_selection != -1 and self.controller.button_clicked(mx, my):
                            if first != turn:
                                top = self.controller.top()
                                if is_winner(hand[turn][my_selection], top):
                                    winner = turn
                            self.controller.place_card(hand[turn], my_selection)
                            turn = (turn + 1) % self.number
                            my_selection = -1
                        else:
                            my_selection = self.select_card(mx,my,hand[turn],my_selection)

                    elif turn != my_turn:
                        # daca pun prima carte, o pun cum vreau, si avansez pointer-ul la urmatorul
                        length = len(hand[turn])
                        if first == turn and not self.controller.table_name:
                            print("Computer primul")
                            card_idx = random.randint(0, length-1)
                        else:
                            possibilities = evaluate(hand[turn], self.controller.top())
                            if possibilities:
                                print(possibilities)
                                card_idx = random.choice(possibilities)
                                winner = turn
                            elif length != 1:
                                card_idx = random.randint(0, length-1)
                            else:
                                card_idx = 0
                        # indiferent ce, computer-ul pune o carte
                        self.controller.place_card(hand[turn],card_idx,enemy=True)
                        self.controller.display_hand(hand[my_turn])
                        pygame.display.flip()
                        turn = (turn + 1) % self.number
                        round_ended = True

            self.controller.toggle_rectangle(mx,my)


players = list()
players.append(Player("Daniel"))
players.append(Player("Computer"))
Game(players).start(0)




