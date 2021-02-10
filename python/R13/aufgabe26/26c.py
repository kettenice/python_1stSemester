'''
Implementieren Sie die Fibonacci-Funktion aus der Übung 7.
Die Testanwendung fodert den Benutzer zur Eingabe einer 
natürlichen Zahl n auf und gibt daraufhin die ersten n 
Fibonacci-Zahlen aus. 
Sie soll eine aussagekräftige Fehlermeldung ausgeben, 
falls eine negative Zahl eingegeben wird. '''

from fibonacci import fiboRek
print("Bitte geben Sie eine natürlich Zahl ein: ")
x = int(input())

def nfibo(n, FibL):
    
    if x < 0:
        print("Fehler: Funktion akzeptiert nur natürliche Zahlen (Parameterwert negativ)")
    if n > 0:
        nfibo(n-1, FibL)
        print("Wert der " + str(n) + "ten Fibonacci-Folge ist: " + str(fiboRek(n)))
        return FibL.append(fiboRek(n))
L=[]
print(nfibo(x, L), L)
    




