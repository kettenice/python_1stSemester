'''
Implementieren Sie die in der Vorlesung und Übung kennengelernten 
Funktionalitäten von Linkssequenzen mittels Tupeln in Python. 
Definieren Sie am Anfang Ihres Python-Programms empty=(), 
um die in der Vorlesung vorgestellte Schreibweise benutzen zu können. 
Schreiben Sie die folgenden Funktionen:
'''
empty = ()
#expLS = (1, (2, (3, (4, ()))))
# a) first(xs), die das erste Element der Linkssequenz zurückgibt.
def first(xs):
    return xs[0]
#rint("first: ", first(expLS))

# b) rest(xs), die den Rest der Linkssequenz zurückgibt.
def rest(xs):   # erstellt Rest einer Linkssequenz aus Liste
    return xs[1]
#print("rest: ", rest(expLS))
#   Benutzen Sie ab jetzt nur noch fist und rest um auf die Linkssequenzen zuzugreifen. 
# c) fromLtoLseq(L), die eine Liste in eine Linkssequenz umwandelt.
def ArrToLseq(L):
    if len(L) > 0:     # solange die Liste Elemente enthält, öffnet wir einen weiteren Rest Tuple
        return (L[0], ArrToLseq(L[1:]))         
    else:
        return empty    # die Rekursion endet mit leeren Tupel

x = [1 , 2, 3, 4]

#print("LtoLseq: ", ArrToLseq(x)) # (1, (2, (3, (4, ()))))

#print("empty lenght: ", len(()))
#print(  rest(expLS) == expLS[1])
# d) lastElement(xs), die das letzte Element der Linkssequenz zurückgibt.
def lastElement(xs):    
    if rest(xs) != empty:
        return lastElement(rest(xs))
    else:
        return first(xs)
#print("last element: ", lastElement(expLS))
# e) nElement(n,xs), die das nte Element liefert.
def nElement(n, xs):
    if n > len(xs) or n < 1:
        return "Elementindex mind. 1 UND max. Länge der Linkssequenz"
    if n == 1:
        return first(xs)
    else:
        return nElement(n-1, rest(xs)) #2
#print("Gesuchtes Element: ", nElement(2, expLS))
# f) concat(xs,ys), die xs mit ys konkateniert.
def concat(xs,ys):
    if rest(xs) != empty:
        return (first(xs), concat(rest(xs), ys))
    else:
        return (first(xs), ys)
#LS1 = (1, (2, (3, ())))
#LS2 = (7, ())
#print("concat: ", concat(LS1, LS2)) #(1, (2, (3, (7, ()))))

# g) init(xs), die die Linkssequenz bis auf das letzte Element liefert.
def init(xs):
    if rest(xs) != empty:
        return (first(xs), init(rest(xs)))
    else:
        return empty
#print(init(LS2))
# h) reverse(xs), die die Linkssequenz mit umgekehrter Reihenfolge ihrer Elemente zurückgibt.
def reverse(xs):
    if  rest(xs) != empty:
        return (lastElement(xs), reverse(init(xs)))
    else:
        return (lastElement(xs), empty)
#print("reverse: ", reverse(concat(LS1, LS2)))
# i) ls2rs(xs), die zu einer Linkssequenz eine Rechntssequenz mit den gleichen Elementen liefert.
def ls2rs(xs):
    if  rest(xs) != empty:
        return (ls2rs(rest(xs)), first(xs))
    else:
        return (empty, first(xs))
#LS1 = (1, (2, (3, ())))
#print("ls2rs: ", ls2rs(concat(LS1, LS2)))