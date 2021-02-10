'''
Schreiben Sie anonyme Funktionen für die folgenden Probleme:
1. Multiplikation dreier Zahlen
'''
mulDrei = lambda x,y,z: x*y*z
print(mulDrei(2,3,5))

'''
2. (a,b,c,d) → a^1 + b^2 + c^3 + d^4
'''
tupelSum = lambda x: (x[0]**1) + (x[1]**2) + (x[2]**3) + (x[3]**4)
tupel = (4, 3, 2, 1)
print(tupelSum(tupel))


'''
3. Es soll "viel" ausgegeben werden, wenn die Zahl größer als 100 ist und sonst "wenig"
'''
vielWenig = lambda x: "viel" if x > 100 else "wenig"



'''
4. Erstellen Sie (z.B. mit Hilfe der Funktionen aus letzter Woche) eine Linkssequenz 
bestehend aus mehreren anonymen Funktionen. Diese sollen nun nacheinander auf einen 
übergebenen Wert angewandt werden, wobei die Funktionswerte zusammen als eine 
Linkssequenz zurückgegeben werden sollen.
'''
import lxs, lxs_map

value = 5
a, b, c = lambda x: x+1, lambda a: a*2, lambda c: c-10
links = (a, (b, (c, ())))

def func(xs, a):
    if lxs.rest(xs) == lxs.empty:
        return (lxs.first(xs)(a), lxs.empty)
    else:
        return (lxs.first(xs)(a), func(lxs.rest(xs), lxs.first(xs)(a)))

print(func(links, 5)) #(6, (12, (2, ())))

#f = lambda xs: lambda a: (lxs.first(xs)(a), lxs.empty) if lxs.rest(xs) == lxs.empty else (lxs.first(xs)(a), f(lxs.rest(xs))(lxs.first(xs)(a)))
#print(f (links) (5))

''' 
die ersten beiden lambda-Ausdrücke mit nur einem Parameter aufrufen:    
'''
# 1. mulDrei = lambda x,y,z: x*y*z
# 2. tupelSum = lambda x: (x[0]**1) + (x[1]**2) + (x[2]**3) + (x[3]**4)

mulDrei_curry = lambda x: lambda y: lambda z: x*y*z

