# Schreiben Sie jetzt eine Variante von map für Linkssequenzen
from lxs import rest, first, empty
def mapLsec(f, xs):
    
    if rest(xs) == empty:
        return (f(first(xs)), empty)
    else:
        return (f(first(xs)), mapLsec(f, rest(xs)))

