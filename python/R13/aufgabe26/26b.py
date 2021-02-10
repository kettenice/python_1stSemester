'''Eine Funktion, die die Länge einer Liste berechnet.'''

def lenListRek(list):
    if list == []:
        return 0
    else:
        return 1 + lenListRek(list[:-1])

L = [1, 2, 3, 4]

print(lenListRek(L))