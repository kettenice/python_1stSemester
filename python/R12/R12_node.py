
''' 
Ein Objekt kann als Datenelement auch ein weiteres Objekt enthalten. Dadurch kann man größere zusammenhängende Gebilde, 
wie z.B. Graphen, erstellen. Entwerfen Sie eine Klasse Node. Ein Objekt dieser Klasse soll 
einen Knoten eines ungerichteten Graphen modellieren. Dabei soll jedes Objekt der Klasse eine Liste 
aller benachbarten Knoten enthalten. Überlegen Sie sich die benötigten Methoden und implementieren Sie diese.
a) Erstellen Sie mit Ihrer Klasse Node einen ungerichteten Graphen. 
'''
class Node:
    # Knoten eines ungerichteten Graphen modellieren
    # jedes Objekt soll Liste benachbarter Knoten enthalten
    adj = None
    name = None
    
    def __str__(self):
        return str(self.name)

    def __init__(self, v=0):
        self.adj = []
        self.name = v

    def add(self, newnode):
        if newnode not in self.adj:
            self.adj.append(newnode)
            newnode.adj.append(self)
        else:
            print("Node mit selben Namen bereits in Adjazenzliste")
    
    def remove(self, rmnode):
        if rmnode in self.adj:
            self.adj.remove(rmnode)
            rmnode.adj.remove(self)
        else:
            print("Node kann nicht entfernt werden, da nicht in Adjazenzliste")

    def getNeighbors(self):
        return self.adj
'''
b) Schreiben Sie eine Breitensuche, die Ihre Klasse Node benutzt.
'''
def bfs_node(node):             #EINGABE: Startknoten aus einem endlichen Graphen
    akt = node                  #AUSGABE: Knotenliste
    Queue, klist = [akt], [akt]

    while Queue:
        akt = Queue.pop(0)      # Forderster Knoten der Warteschlange wird entfernt und 'akt' zugewiesen
        for nachbar in akt.getNeighbors():
            if not nachbar in klist:
                klist.append(nachbar)
                Queue.append(nachbar)
                print(nachbar)
    

graph = Node(6)
b = Node(3)
c = Node(1)
d = Node(4)
e = Node(2)
graph.add(d)
graph.add(b)
b.add(c)
d.add(c)
d.add(e)
print(bfs_node(graph))