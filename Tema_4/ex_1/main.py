import sys
import turtle
t = turtle.Pen()
screen = turtle.Screen()
turtle.setup(width=1.0, height=1.0)
t.width(5)
t.up()
t.goto(-700,0)
t.down()

def A():
    t.left(60)
    t.forward(80)
    t.right(120)
    t.forward(80)
    t.right(180)
    t.forward(30)
    t.left(60)
    t.forward(50)
    t.up()
    t.left(80)
    t.forward(27)
    t.left(100)
    t.forward(130)
    t.down()


def B():
    t.left(90)
    t.forward(72)
    t.right(90)
    for i in range(45):
        t.forward(1.28)
        t.right(4)
    t.right(180)
    for i in range(45):
        t.forward(1.28)
        t.right(4)
    t.right(180)
    t.up()
    t.forward(100)
    t.down()

def C():
    t.circle(36, 40)
    t.up()
    t.circle(36, 100)
    t.down()
    t.circle(36, 220)
    t.up()
    t.forward(100)
    t.down()

def D():
    t.circle(36, 180)
    t.left(90)
    t.forward(72)
    t.left(90)
    t.up()
    t.forward(110)
    t.down()

def E():
    t.forward(50)
    t.up()
    t.backward(50)
    t.down()
    t.left(90)
    t.forward(36)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(36)
    t.right(90)
    t.forward(50)
    t.up()
    t.right(90)
    t.forward(72)
    t.left(90)
    t.forward(80)
    t.down()

def F():
    t.left(90)
    t.forward(36)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(36)
    t.right(90)
    t.forward(50)
    t.up()
    t.right(90)
    t.forward(72)
    t.left(90)
    t.forward(100)
    t.down()

def G():
    t.circle(36,90)
    t.left(90)
    t.forward(36)
    t.backward(36)
    t.right(90)
    t.up()
    t.circle(36, 30)
    t.down()
    t.circle(36, 240)
    t.up()
    t.forward(100)
    t.down()

def H():
    t.left(90)
    t.forward(72)
    t.backward(36)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(36)
    t.backward(72)
    t.right(90)
    t.up()
    t.forward(90)
    t.down()

def I():
    t.left(90)
    t.forward(72)
    t.backward(72)
    t.right(90)
    t.up()
    t.forward(90)
    t.down()

def J():
    t.circle(36, 90)
    t.forward(36)
    t.up()
    t.backward(72)
    t.right(90)
    t.forward(90)
    t.down()

def K():
    t.left(90)
    t.forward(72)
    t.backward(36)
    t.right(45)
    t.forward(51)
    t.backward(51)
    t.right(90)
    t.forward(51)
    t.backward(51)
    t.left(45)
    t.up()
    t.forward(130)
    t.right(90)
    t.forward(36)
    t.left(90)
    t.down()

def L():
    t.forward(36)
    t.backward(36)
    t.left(90)
    t.forward(72)
    t.up()
    t.right(90)
    t.forward(130)
    t.right(90)
    t.forward(72)
    t.left(90)
    t.down()

def M():
    t.left(90)
    t.forward(72)
    t.right(135)
    t.forward(50.4)
    t.left(90)
    t.forward(50.4)
    t.right(135)
    t.forward(72)
    t.up()
    t.left(90)
    t.forward(100)
    t.down()

def N():
    t.left(90)
    t.forward(72)
    t.right(135)
    t.forward(100.8)
    t.left(135)
    t.forward(72)
    t.backward(72)
    t.up()
    t.right(90)
    t.forward(100)
    t.down()

def O():
    t.circle(36)
    t.up()
    t.forward(100)
    t.down()

def P():
    t.left(90)
    t.forward(72)
    t.left(90)
    t.up()
    t.circle(18, 180)
    t.down()
    t.circle(18, 180)
    t.up()
    t.left(90)
    t.forward(72)
    t.left(90)
    t.forward(110)
    t.down()

def Q():
    t.circle(36, 45)
    t.right(90)
    t.forward(30)
    t.backward(30)
    t.left(90)
    t.circle(36, 315)
    t.up()
    t.forward(110)
    t.down()

def R():
    t.left(90)
    t.forward(72)
    t.left(90)
    t.up()
    t.circle(18, 180)
    t.down()
    t.circle(18, 180)
    t.up()
    t.circle(18, 180)
    t.down()
    t.right(45)
    t.forward(50.4)
    t.backward(50.4)
    t.up()
    t.left(45)
    t.forward(110)
    t.right(90)
    t.forward(36)
    t.left(90)
    t.down()

def S():
    t.left(90)
    t.up()
    t.forward(18)
    t.down()
    t.left(180)
    t.circle(18, 270)
    t.right(180)
    t.up()
    t.circle(18, 90)
    t.down()
    t.circle(18, 270)
    t.up()
    t.forward(110)
    t.right(90)
    t.forward(36)
    t.left(90)
    t.down()

def T():
    t.left(90)
    t.forward(72)
    t.left(90)
    t.forward(30)
    t.backward(60)
    t.left(90)
    t.up()
    t.forward(72)
    t.left(90)
    t.forward(80)
    t.down()

def U():
    t.up()
    t.left(90)
    t.forward(72)
    t.right(180)
    t.down()
    t.forward(36)
    t.circle(36, 180)
    t.forward(36)
    t.up()
    t.backward(72)
    t.right(90)
    t.forward(100)
    t.down()

def V():
    t.up()
    t.left(90)
    t.forward(72)
    t.right(150)
    t.down()
    t.forward(83)
    t.left(120)
    t.forward(83)
    t.up()
    t.right(150)
    t.forward(72)
    t.left(90)
    t.forward(80)
    t.down()

def W():
    t.up()
    t.left(90)
    t.forward(72)
    t.right(150)
    t.down()
    t.forward(83)
    t.left(120)
    t.forward(83)
    t.right(120)
    t.forward(83)
    t.left(120)
    t.forward(83)
    t.up()
    t.right(150)
    t.forward(72)
    t.left(90)
    t.forward(100)
    t.down()

def X():
    t.left(60)
    t.forward(83)
    t.backward(41.5)
    t.left(60)
    t.forward(41.5)
    t.backward(83)
    t.right(120)
    t.up()
    t.forward(100)
    t.down()

def Y():
    t.left(90)
    t.forward(36)
    t.right(30)
    t.forward(41.5)
    t.backward(41.5)
    t.left(60)
    t.forward(41.5)
    t.backward(41.5)
    t.right(30)
    t.up()
    t.backward(36)
    t.right(90)
    t.forward(100)
    t.down()

def Z():
    t.forward(72)
    t.backward(72)
    t.left(45)
    t.forward(100.8)
    t.left(135)
    t.forward(72)
    t.up()
    t.backward(172)
    t.left(90)
    t.forward(72)
    t.left(90)
    t.down()

def Punkt():
    t.circle(1)
    t.up()
    t.forward(100)
    t.down()

def Fragezeichen():
    t.circle(1)
    t.left(90)
    t.up()
    t.forward(20)
    t.down()
    t.forward(16)
    t.right(90)
    t.circle(18,210)
    t.up()
    t.circle(18, 150)
    t.right(90)
    t.forward(36)
    t.left(90)
    t.forward(100)
    t.down()

def Aufrufezeichen():
    t.circle(1)
    t.up()
    t.left(90)
    t.forward(20)
    t.down()
    t.forward(52)
    t.up()
    t.backward(72)
    t.right(90)
    t.forward(100)
    t.down()

def enter():
    sys.exit()

def alternativ():
    screen.onkeypress(lambda: t.left(45), 'a')
    screen.onkeypress(lambda: t.right(45), 'd')
    screen.onkeypress(lambda: t.up(), 'f')
    screen.onkeypress(lambda: t.down(), 'g')
    screen.onkeypress(lambda: t.backward(10), 's')
    screen.onkeypress(lambda: t.forward(10), 'w')

def W2():
    f = open('neue_zeichen.py', 'r+')
    c = f.read()
    f = open('neue_zeichen.py', 'w+')
    f.write(c)
    t.forward(10)
    f.write('t.forward(10)\n    ')
    f.close()

def S2():
    f = open('neue_zeichen.py', 'r+')
    c = f.read()
    f = open('neue_zeichen.py', 'w+')
    f.write(c)
    t.backward(10)
    f.write('t.backward(10)\n    ')
    f.close()

def D2():
    f = open('neue_zeichen.py', 'r+')
    c = f.read()
    f = open('neue_zeichen.py', 'w+')
    f.write(c)
    t.right(45)
    f.write('t.right(45)\n    ')
    f.close()

def A2():
    f = open('neue_zeichen.py', 'r')
    c = f.read()
    f = open('neue_zeichen.py', 'w')
    f.write(c)
    t.left(45)
    f.write('t.left(45)\n    ')
    f.close()

def F2():
    f = open('neue_zeichen.py', 'r')
    c = f.read()
    f = open('neue_zeichen.py', 'w')
    f.write(c)
    t.up()
    f.write('t.up()\n    ')
    f.close()


def G2():
    f = open('neue_zeichen.py', 'r')
    c = f.read()
    f = open('neue_zeichen.py', 'w')
    f.write(c)
    t.down()
    f.write('t.down()\n    ')
    f.close()

def speichern(neu, neu1):
    f = open('neue_zeichen.py', 'r+')       #das speichert as neue zeichen in den worterbuch neue_zeichen
    content = f.read()
    f = open('neue_zeichen.py', 'w')
    f.write(content)
    f.write('\nneue_zeichen[' + '"' + neu1 + '"' + '] = ' + neu)
    f.close()


from neue_zeichen import *


def zeichnen():
    import string
    default = {}
    alfa_functii = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
    for i in range(26):
        default[string.ascii_lowercase[i]] = alfa_functii[i]   #Ein Worterbuch definieren, der alle Zeichen als key
    default['.'] = Punkt                              #hat und alle Funktionen als Values hat
    default['!'] = Aufrufezeichen
    default['?'] = Fragezeichen
    default['Return'] = enter
    neu = {}     #das neu-Worterbuch enthalt die neue Zeichen
    for key, value in neue_zeichen.items():
        neu[key] = value
    for i in default.keys():
        screen.onkeypress(default[i], i)      #
    for key in neu.keys():
        screen.onkeypress(lambda: neu[key](t), key)

    caractere =list(string.printable)

    for p in string.ascii_letters:
        if p in caractere:              #Hier alle Zeichen, die keine entsprechende Funktionen haben, werden in eine
            caractere.remove(p)         #Liste gesteckt. Wenn diese gedruckt werden, kann man selbst mit wasd zeichnen
    caractere.remove('?')
    caractere.remove('!')
    caractere.remove('.')
    for char in list(neue_zeichen.keys()):
        caractere.remove(char)
    for i in caractere:
        screen.onkeypress(alternativ, i)


    screen.listen()
    n = input('Was soll ich schreiben: ')
    for k in n.lower():
        if k in default.keys():
            default[k]()
        if k in neu.keys():
            neu[k](t)




def start():
    entscheidung = int(input("""
    1. Textnachricht zeichnen
    2. Neues Zeichen hinzufugen
    
    """))                           #Hier ist das menu des Aufgabes
    if entscheidung == 1:
        zeichnen()
    if entscheidung == 2:
        neues_zeichen()


def neues_zeichen():
    import string
    function_letter = 0
    neu = input('Unter welchen Zeichen soll das sein: ')
    neu1 = neu
    caractere = list(string.printable)
    for p in string.ascii_letters:
        if p in caractere:
            caractere.remove(p)
    caractere.remove('?')
    caractere.remove('!')
    caractere.remove('.')
    for char in list(neue_zeichen.keys()):
        caractere.remove(char)
    char = list(string.ascii_lowercase)
    for i in range(len(neue_zeichen)):  #Jede Funktion in ex_4 bekommt eine andre kleine Buchstabe als Name
        function_letter +=1
    if neu in caractere:
        neu = char[function_letter]
    f = open('neue_zeichen.py', 'r+')
    alt = f.read()
    f = open('neue_zeichen.py', 'w+')
    f.write(alt)
    f.write('\ndef ' + neu+'(t):\n    ')
    screen.onkeypress(W2, 'w')      #hier schreibt zeichnet man die neue Zeichnung und die commands
    screen.onkeypress(S2, 's')      #werden in ein anderes file gesteckt
    screen.onkeypress(A2, 'a')
    screen.onkeypress(D2, 'd')
    screen.onkeypress(F2, 'f')
    screen.onkeypress(G2, 'g')
    screen.onkeypress(lambda: speichern(neu, neu1), ' ')
    screen.listen()

    f.close()


start()

turtle.done()
