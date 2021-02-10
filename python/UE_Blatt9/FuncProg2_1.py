'''
Ersetzen Sie in der folgenden Funktionsdefinition die Parameter f, a, seq so, dass die Fakulta ̈tsfunktion definiert wird:
def fakReduce(n):
return reduce(f,seq,a)
'''
from functools import reduce

def fakReduce(n):
    return reduce(lambda x,y: x*y,list(range(1,n+1)),1)

print(fakReduce(5))

