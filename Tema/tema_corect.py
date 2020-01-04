"""
Exercitiu cu tehnici de cautare (50min)
************************************************************************************************
  Se considera o multime de oameni fiecare om avand o submultime dintre acestia trecuti
pe un contact-list (de exemplu de mail sau messenger).
  Se presupune ca fiecare nume e format din doar 2 cuvinte separate printr-un
spatiu : 'Prenume Nume'
  Se considera ca oamenii nu stiu ce prieteni au altii pe contact-list-ul lor. Unul dintre ei
isi cauta un fost prieten din copilarie, din al carui nume nu-si mai aminteste decat
initialele.
  El scrie un mesaj in care ii roaga pe toti cei care il primesc sa il trimita
mai departe catre prietenii lor si apoi il trimite catre toti prietenii pe care ii are
in contact list.
  Cei care primesc mesajul vad toata lista de forwarduri si nu vor
trimite mesajul celor care l-au primit deja (ca sa nu ii enerveze pe cei pe la care a
mai trecut mesajul).
  Totusi daca primesc acelasi mesaj din surse diferite nu se vor mai uita pe lista de forward
al celuilalt mesaj (se considera ca nu se mai complica si cu a revedea un mesaj anterior ci
se uita doar pe mesajul curent).
  Deci practic conteaza doar calea urmata de mesajul curent.
  Unii oameni care primesc mesajul insa pot fi ocupati, motiv pentru care nu se vor
lasa convinsi sa trimita mai departe mesajul decat dupa ce il vor primi de mai multe ori.
  Cei liberi trebuie sa il primeasca doar o data ca sa il trimita mai departe. Cei ocupati
de cel putin 2 ori (nu vor trimite un mesaj daca nu il primesc doar o data).
  Cei foarte ocupati de cel putin 3 ori ca sa trimita mesajul mai departe.
"""  # cerinta
"""
 In concluzie avem 3 stari posibile in care se poate afla o persoana si in functie de care
persoana respectiva alege cat sa astepte pana trimite mesajul:
    * liber
    * ocupat
    * foarte ocupat

 Se considera ca a ajuns un mesaj in momentul in care a fost generat un succesor in graf.
"""  # stari
"""
 Fisierul de intrare va avea urmatoarea forma. Pe primul rand vom avea:
    Initiala1    Initiala2      NumeCautator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programul va face astfel incat pentru fiecare persoana cu acele initiale sa se arate
lantul de e-mailuri prin care a ajuns prima oara (cronologic) mesajul la el.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pe urmatoarele randuri din fisier, pana la finalul fisierului, vom avea trecute toate
persoanele luate in vedere de algoritm. Fiecarei persoane ii corespunde un rand.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pe randul respectiv se gasesc informatiile:
NumePersoana    Stare    Prieten_1 Prieten_2 ... Prieten_k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In fisierul de iesire, solutiile vor fi scrise sub forma Nume1->Nume2->....NumeK
unde Nume1 e cel care a expediat prima oara mesajul, Nume 2 l-a primit de la Nume 1
si l-a trimis la Nume 3, NumeK e ultimul care a primit mesajul.
"""  # format fisier
"""
 Precizari:
  * In scrierea functiei de afisare a unei solutii, se considera garantat faptul ca sunt minim
  2 noduri intr-o solutie - nu poate chiar cel care cauta sa fie prietenul pe care il cauta.
  * Se garanteaza faptul ca persoana care isi cauta prietenul are starea liber (deci poate
  trimite mesajele)
  * Fiecare persoana din date va avea lista de prieteni scrisa in fisier. Nu exista persoane
  care sa apara pe o lista de prieteni a cuiva dar sa nu aiba popria lista de prieteni scrisa.
  * Se garanteaza faptul ca exista cel putin o persoana in fisier.
  * Nu exista oameni fara prieteni (intr-o lume ideala...)
  * Numele persoanelor se scriu intre ghilimele deoarece contin mai multe cuvinte
  (minim doua: prenume si nume)
"""  # precizari
"""
Pentru fisierul:
    D G 'Ion Popescu'
    'Ion Popescu' liber 'George Danescu' 'Dan Georgescu' 'Ion Costescu'
    'George Danescu' foarte_ocupat 'Ion Popescu' 'Ion Costescu' 'Dan Georgescu' 'Lia Dobrescu' 'Diana Gigescu'
    'Dan Georgescu' liber 'Ion Popescu' 'George Danescu'
    'Ion Costescu' liber 'Ion Popescu' 'Daria Geescu' 'Lia Dobrescu' 'George Danescu'
    'Lia Dobrescu' ocupat 'George Danescu' 'Ion Costescu' 'Daniel Gegescu'
    'Diana Gigescu' liber 'George Danescu'
    'Daniel Gegescu' liber 'Lia Dobrescu'
    'Daria Geescu' liber 'Ion Costescu' 'Teodor Andreescu'
    'Teodor Andreescu' liber 'Daria Geescu'

avem rezultatul (primele 4 solutii):
    Ion Popescu->Dan Georgescu
    Ion Popescu->Ion Costescu->Daria Geescu
    Ion Popescu->George Danescu->Diana Gigescu
    Ion Popescu->Ion Costescu->Lia Dobrescu->Daniel Gegescu

"""  # expl1
"""
Pentru fisierul: (unde am sters relatia de prietenie dintre Ion Costescu si George Danescu)
    D G 'Ion Popescu'
    'Ion Popescu' liber 'George Danescu' 'Dan Georgescu' 'Ion Costescu'
    'George Danescu' foarte_ocupat 'Ion Popescu'  'Dan Georgescu' 'Lia Dobrescu' 'Diana Gigescu'
    'Dan Georgescu' liber 'Ion Popescu' 'George Danescu'
    'Ion Costescu' liber 'Ion Popescu' 'Daria Geescu' 'Lia Dobrescu'
    'Lia Dobrescu' ocupat 'George Danescu' 'Ion Costescu' 'Daniel Gegescu'
    'Diana Gigescu' liber 'George Danescu'
    'Daniel Gegescu' liber 'Lia Dobrescu'
    'Daria Geescu' liber 'Ion Costescu' 'Teodor Andreescu'
    'Teodor Andreescu' liber 'Daria Geescu'

Avem rezultatul:
    Ion Popescu->Dan Georgescu
    Ion Popescu->Ion Costescu->Daria Geescu

Observati ca desi ar fi existat cai posibile de ajungere si la Diana Gigescu si la
Daniel Gegescu lantul de mesaje trecea pe la cineva foarte ocupat care nu a mai primit
destule mesaje pentru a fi convins sa trimita mesajul mai departe.
"""  # expl2
"""
Indicatie: un nod reprezinta o persoana, iar numarul de dati in care a primit mesajul este
dat de numarul de aparitii ale persoanei respective in arborele de parcurgere.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pentru fiecare dintre cei 3 algoritmi (BF, DF, DFI):
  * afisati timpii de executie
  * afisati memoria maxim utilizata in cadrul rularii
  * opriti executia algoritmului respectiv daca depaseste timpul de timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parametrii programului vor fi in ordine:
  * timpul de timeout (dat in secunde)
  * numarul de solutii de afisat (in fisierul de output solutiile vor fi separate prin 2 linii
  noi vide, urmate de o linie cu 10 caractere #, urmate de alte doua linii noi vide). E posibil
  sa nu apara in fisier numarul de solutii dorit, daca nu exista atatea solutii sau cautarea
  s-a terminat cu timeout.
  * fisierul de input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Numele programului este obligatoriu tema1.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Numele fisierelor de input va fi de forma inputsufix.txt iar outputul va fi de forma outputsufix.txt
De exemplu, daca avem fisierul input_date17.txt, atunci fisierul de output va fi output_date17.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Barem (punctajul e dat in procentaje din punctajul maxim al temei; procentajul maxim este 100%):
  * citire din fisier                                                                       (10%)
  * functia de generare a succesorilor                                                      (25%)
  * functia de testare a scopului                                                           (10%)
  * rularea cu fiecare algoritm dintre cei 3                                          (3*5% =15%)
  * afisarea in fisierele de output in formatul cerut                                       (15%)
  * afisarea timpilor pentru fiecare dintre cei 3 algoritmi                                  (5%)
  * calcularea memoriei maxime utilizate pentru fiecare dintre cei 3 algoritmi               (5%)
  * crearea a 5 fisiere de input care sa arate diferente intre cei 3 algoritmi:       (5*2% =10%)
     - un fisier de input care nu are solutii
     - doua fisiere de input care ruleaza bine pe cei 3 algoritmi (avand solutii de lungime cel putin 10)
     - un fisier de input care blocheaza BF-ul din cauza memoriei ocupate sau a timpului folosit (dar unul
     dintre ceilalti doi algoritmi duc la o solutie)
     - un fisier de input care blocheaza DF-ul (calculul dureaza prea mult fiindca s-a dus in jos pe o ramura prea
     lunga sau chiar infinita) insa unul dintre ceilalti doi algoritmi duc la o solutie.
  * documentatie (intr-un fisier txt): explicarea algoritmului de generare a succesorilor,
  scrierea intr-un fisier a outputului (timpi+memorie) pentru cei 3 algoritmi si
  explicarea/analizarea rezultatelor.                                                        (5%)

  Inainte de a scrie in documentatie timpul de executie pentru un algoritm rulati programul
de mai multe ori si luati o valoare medie, deoarece timpul de executie poate sa difere si
in functie de alte procese care ruleaza in acelasi timp.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Se poate da bonus pentru algoritmi foarte eficienti sau un mod elegant si eficient de programare
(exemple: evitarea repetarii codului: se va pune in functii si se va apela unde e nevoie in loc sa
fie luat cu copy-paste prin program, modularizare, folosirea expresiilor regulate, list comprehensions,
gasirea celui mai eficient mod de calculare a succesorilor etc.).
  Bonusul este pana la un maxim de 10% in functie de eficienta si organizarea codului.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bonus.
  Generarea aleatoare a datelor de intrare: se va face un program separat care primeste ca parametri
datele necesare pentru generarea unor fisiere de input. Unul dintre parametri este obligatoriu numarul
de fisiere de input care trebuie generate. La prezentare se va rula programul pe acele fisiere de input.
(bonusul e pana la maxim 15% in functie de cat de complexa este generarea: daca se pot genera si cazuri
particulare, cat la suta din fisierele de intrare au solutii (de un exemplu bun ar fi: 90% au solutii si
doar 10% nu au)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bonus.(pana la 5% din punctaj)
  Posibilitate de a specifica mai multe fisiere de input in linia de comanda la un singur apel al
programului (fie prin enumerarea lor in linia de comanda, fie prin specificarea folderului in care se
afla toate - si programul le va prelua de acolo).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Tema nu se puncteaza fara prezentare.
  - Se va da o nota pe prezentare de la 1 la 10 in functie de cat de bine a stiut studentul sa explice ce
a facut.
  - Punctajul temei se va inmulti cu nota_prezentare/10. Astfel, daca cineva stie sa explice doar jumatate
din ce a facut, primeste jumatate din punctaj; daca nu stie nimic primeste 0.
"""  # barem

import numpy as np


class Info:
    def __init__(self, name, state, friends):
        self.name = name
        self.state = state
        self.friends = friends
        self.initials = [l[0] for l in name]


class NodParcurgere:
    def __init__(self, idx, info, parinte):
        self.idx = idx  # este indicele din vectorul de noduri
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere

    def obtineDrum(self):
        l = [self.info]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte.info)
            nod = nod.parinte
        return l

    def afisDrum(self):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        print("->".join(l))
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if infoNodNou == nodDrum.info:
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        sir = ""
        sir += self.info + "("
        sir += "id = {}, ".format(self.idx)
        sir += "drum="
        drum = self.obtineDrum()
        sir += "->".join(drum)
        sir += ")"
        return sir


class Node:
    def __init__(self, name, state, friends, idx):
        self.info = Info(name,state,friends)
        self.idx = idx

    def to_string(self):
        my_str  = str(self.idx) + ") " + "".join(self.info.initials) + ' - '
        my_str += " ".join(self.info.name) + " (%s): " %self.info.state
        my_str += ", ".join([" ".join(fr) for fr in self.info.friends])
        return my_str

    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

    def __eq__(self, other):
        return self.info.name == other.info.name


class Graph:  # graful problemei
    def __init__(self, noduri, matrice, neighbours, v_e, start, scopuri):
        self.noduri = noduri
        self.matrice = matrice
        self.neighbours = neighbours
        self.v_e = v_e
        self.nrNoduri = len(matrice)
        self.start = start
        self.scopuri = scopuri

    def indiceNod(self, n):
        return self.noduri.index(n)

    def genereazaSuccesori(self, nodCurent):
        listaSuccesori = []
        for i in range(self.nrNoduri):
            if self.matrice[nodCurent.idx][i] == 1 and \
               not nodCurent.contineInDrum(self.noduri[i]):
                nodNou = NodParcurgere(i, self.noduri[i], nodCurent)
                listaSuccesori.append(nodNou)
        return listaSuccesori

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return sir


def get_contacts(file):
    with open(file,'r') as f:
        temp = f.readline().replace("'",'').split()
        initials, my_name = temp[0:2], temp[2:]
        print("\nInitialele: ", *initials)
        lines = [l.replace("'",'').split() for l in f.readlines()]
        contacts = list()
        nodes = list()
        for idx,line in enumerate(lines):
            name,state = line[:2],line[2]
            friends = [(line[i],line[i+1]) for i in range(3,len(line),2)]
            contacts.append(Node(name,state,friends,idx))
            nodes.append(" ".join(name))

    print("\nContinut fisier:")
    print('\t' + "\n\t".join([str(fr) for fr in contacts]))

    return contacts, nodes, initials



def same_initials(name,initials):
    temp_arr = [i[0] for i in name.split()]
    return temp_arr == initials

def as_graph(contacts, nodes,initials):
    matrix = np.zeros((len(contacts), len(contacts)), 'int8')
    neighbours = dict()
    vertices = list()
    edges = list()
    print("\nAsociere nume->nr:")
    for contact in contacts:
        print('\t'+str(contact.idx), end=": ")
        vertices.append(contact.idx)
        temp_list = list()
        for friend in contact.info.friends:
            idx = nodes.index(" ".join(friend))
            print(idx, end=' ')
            matrix[contact.idx][idx] = 1
            temp_list.append(idx)
            edges.append((contact.idx, idx))
        neighbours[contact.idx] = temp_list
        print()
    v_e = dict()
    v_e["vertices"] = vertices
    v_e["edges"] = edges
    symmetric = np.sum([(a == b) for (a,b) in zip(matrix, np.transpose(matrix))]) == len(contacts)**2

    print("\nMatrix:\n", matrix)
    print("\nNeighbours:\n", neighbours)
    print("\nVertices\Edges:\n", v_e)
    print("\nGraf Neorientat") if symmetric else print("\nGraf Orientat")

    scopuri = [k for k in nodes if same_initials(k,initials)]
    print("\nScopuri: ", scopuri)
    return Graph(nodes,matrix, neighbours, v_e, nodes[0], scopuri)



#### algoritm BF
# presupunem ca vrem mai multe solutii (un numar fix)
# daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# si doar oprim algoritmul la afisarea primei solutii

def breadth_first(gr):
    nrSolutiiCautate = 4
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.noduri.index(gr.start), gr.start, None)]

    continuaa = True  # variabila pe care o setez la false cand consider ca s-au afisat suficiente solutii
    scopuri = gr.scopuri.copy()
    while len(c) > 0 and continuaa:
        nodCurent = c.pop(0)

        if nodCurent.info in scopuri:
            nodCurent.afisDrum()
            nrSolutiiCautate -= 1
            scopuri.remove(nodCurent.info)

            if nrSolutiiCautate == 0:
                continuaa = False
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        c.extend(lSuccesori)



continua = True


def depth_first(gr):
    # vom simula o stiva prin relatia de parinte a nodului curent
    df(NodParcurgere(gr.noduri.index(gr.start), gr.start, None),gr)

nrSolutiiCautate = 4
def df(nodCurent,gr):
    global continua, nrSolutiiCautate
    if not continua:
        return

    if nodCurent.info in gr.scopuri:
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            continua = False

    lSuccesori = gr.genereazaSuccesori(nodCurent)
    for sc in lSuccesori:
        df(sc,gr)


def depth_first_iterative_deepening(gr, adancimeMaxima):
    # vom simula o stiva prin relatia de parinte a nodului curent
    for i in range(1, adancimeMaxima):
        dfi(i, NodParcurgere(gr.noduri.index(gr.start), gr.start, None),gr)


# e exact ca functia df din laboratorul anterior doar ca impunem si o lungime maxima a drumului
nrSol = 5
continuaaa = True
def dfi(adMaxCurenta, nodCurent,gr):
    global nrSol, continuaaa
    # descrestem adMaxCurenta pana la 0
    if adMaxCurenta <= 0 or not continuaaa:  # ar trebui adMaxCurenta sa nu ajunga niciodata < 0
        return
    adMaxCurenta -= 1

    if nodCurent.info in gr.scopuri:
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        input()
        nrSol -= 1
        if nrSol == 0:
            continuaaa = False
    lSuccesori = gr.genereazaSuccesori(nodCurent)
    for sc in lSuccesori:
        dfi(adMaxCurenta, sc,gr)


def test(file):
    contacts, nodes, initials = get_contacts(file)

    my_graph = as_graph(contacts, nodes,initials)

    print("\n\nBFS:")
    breadth_first(my_graph)
    print("\nDFS:")
    depth_first(my_graph)
    print("\nDFSI:")
    depth_first_iterative_deepening(my_graph,5)

test("file.txt")




