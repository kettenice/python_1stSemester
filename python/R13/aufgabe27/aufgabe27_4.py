# Schreiben Sie jetzt eine Variante von map für Linkssequenzen
from aufgabe27_3 import rest, first, empty
def mapLsec(f, xs):
    
    if rest(xs) == empty:
        return (f(first(xs)), empty)
    else:
        return (f(first(xs)), mapLsec(f, rest(xs)))

LS = (2, (4, (6, (98, (2, ())))))
newList = mapLsec(lambda x: int(x**x), LS)
print(newList)