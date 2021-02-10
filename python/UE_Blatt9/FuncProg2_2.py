from math import sqrt
m = 2%3
print(m)

def siebErathosFun(n):
    teilerEnt = lambda i: if t%i == 0: False
    nZahlen = list(range(n+1))
    prim = list(filter(teilerEnt, nZahlen))

print(siebErathosFun(20))
'''
Hinweis: 
Beginnen Sie mit einer Liste, die alle Zahlen bis n enthalt.
 Nutzen Sie fortlaufend die Filter-Funktion, um Vielfache 
 bisheriger Primzahlen aus dem Rest der Liste herauszufiltern.

Sie haben bereits das Sieb des Eratosthenes kennen gelernt. 
Diesen Algorithmus sollen Sie nun funktional implementieren.
Schreiben Sie eine Funktion, die eine Zahl n als Parameter 
übergeben bekommt und alle Primzahlen bis n als Python-Liste 
zurück gibt!

    for i in gestrichen:
        i = False
    for i in range(2, sqrt(n)+1):
        if gestrichen[i] == False:
            print(i)
            for j in range(i*i, n+1, i):
                gestrichen[j] = True
    for i in range(sqrt(n)+1, n+1):
        if gestrichen[i] == False:
            print(i)
'''