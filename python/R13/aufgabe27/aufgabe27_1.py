'''
Benutzen Sie Pythons map, reduce, filter Funktionen 
um die folgenden Algorithmen auf Listen zu implementieren.
'''
# a) Alle Werte einer Liste werden auf -1 gesetzt.
def mapNegOne(liste):
    return list(map(lambda x: -1, liste))

L = [1, 2, 4, 5, 6, 7]
print(mapNegOne(L))     #[-1, -1, -1, -1, -1, -1]

# b) Alle geraden Elemente aus einer Liste werden aus der Liste entfernt.
def filterOdd(liste):
    return list(filter(lambda x: x%2 == 1, liste))

L = [1, 2, 4, 5, 6, 7]
print(filterOdd(L))     #[1, 5, 7]

# c) Die Länge einer Liste wird errechnet.
from functools import reduce
def lenghtList(liste):
    return reduce(lambda x, y: x + 1, liste)
L = [1, 2, 4, 5, 6, 7]
print(lenghtList(L))     # 6