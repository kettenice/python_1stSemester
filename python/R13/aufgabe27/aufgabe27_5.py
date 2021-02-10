'''
Verwenden Sie Ihre Funktion map, sodass das folgenden Verhalten implementiert
wird:
a) die Werte aller Elemente der Linkssequenz werden verdoppelt,
b) alle Werte der Linkssequenz werden auf 0 gesetzt,
c) an Stelle jedes Elements wird die Länge seiner String-Repräsentation geschrie- ben.
'''
from aufgabe27_3 import first, rest, empty
from aufgabe27_4 import mapLsec

LS = (2, (4, (6, (98, (2, ())))))
double = mapLsec(lambda x: int(x*2), LS)
setZero = mapLsec(lambda x: 0, LS)
lenStrRep = mapLsec(lambda x: len(str(x)), LS)
print(double)
print(setZero)
print(lenStrRep)