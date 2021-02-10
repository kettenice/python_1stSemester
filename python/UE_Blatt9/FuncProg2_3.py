'''
Schreiben Sie eine Funktion, die aus einer gegebenen Linkssequenz 
eine Rechtssequenz ge- neriert, 
wobei die Elemente in derselben Reihenfolge bleiben!
'''

def ls2rs(xs):
    empty = ()
    if  xs[1] == empty:
        return (empty, xs[0])
    else:
        return (ls2rs(xs[1]), xs[0])
LS = (1, (2, (3, ())))
print(ls2rs(LS))