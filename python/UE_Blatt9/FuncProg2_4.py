'''
Definiert seien drei Funktionen:
h berechnet den Durchschnitt von drei ganzen Zahlen
g rundet eine reelle Zahl auf die na ̈chste Ganzzahl ab
f erwartet zwei Funktionen und drei ganze Zahlen als Eingabe, so dass gilt: Werden die Funktionen h und g u ̈bergeben, dann gibt f den abgerundeten Durchschnitt der drei u ̈bergebenen Zahlen zuru ̈ck.
(a) Geben Sie Definitions-, Wertebereich und Ordnung der Funktionen an!
(b) Schreiben Sie den Definitionsbereich von f so um, dass f
 eine Komposition der beiden Funktionen h und g erhalten kann, also nur noch eine Funktion und drei ganze Zahlen u ̈bergeben bekommt, aber die gleiche Abbildung realisiert, wie zuvor!
(c) Schreiben Sie die Funktion h vollsta ̈ndig gecurried auf! 
Wie sieht ein Aufruf der Funk- tion fu ̈r die Zahlen (a = 2,b = 5,c = 5) aus?
'''

def compareTriplets(a, b):
    cp = [0, 0]
    for i in range(0, 3):
        if (a[i] < b[i]):
            cp[1] = cp[1] + 1
        if (a[i] > b[i]):
            cp[0] = cp[0] + 1
    return cp

x = (4, 5, 2)
y = (1, 2, 3)

xy = compareTriplets(x,y)
print(xy)