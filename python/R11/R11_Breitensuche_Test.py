
def bfs_shortestPath(adjL, start, ziel):       #EINGABE: Start -UND Endknoten aus einem endlichen Graphen
    Q, mark = [], []                           #AUSGABE: Liste mit kürzestem Weg
    
    for i in adjL:
        mark.append(-1)
    mark[start] = 0
    Q.append(start)
    while Q:
        akt = Q.pop(0)
        for nachbar in adjL[akt]:
            if mark[nachbar] == -1:
                mark[nachbar] = 1 + mark[akt]
                print("Mark", mark)
                Q.append(nachbar)
                print("Queue", Q)
    
    if mark[ziel] == -1:
        #print("test")
        return -1

    L = [ziel]
    akt = ziel

    while akt != start:
        nachbarn = adjL[akt]
        #akt = nachbarn[0]
        for k in nachbarn:
            if mark[k] < mark[akt]:
                akt = k
        L.append(akt)
        print("Liste", L)
    #print("test")

    return print(L[::-1])
# Name  TXL     CGN     FRA     MUC     KEL     STR     PAD     SFX
# Index  7      0       1       3       2        5       4        6
Flughaefen = [[3, 7], [2, 3, 5], [1], [0, 1, 4, 6], [3], [1], [3], [0, 1]]

wert = bfs_shortestPath(Flughaefen, 4, 2)
