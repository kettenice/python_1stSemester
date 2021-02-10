
'''
Die Multiplikation zweier natürlicher Zahlen, die nur auf der Addition basiert.
Die Testanwendung fodert den Benutzer zur Eingabe zweier natürlicher Zahlen auf 
und berechnet deren Produkt durch Aufruf der rekursiven Funktion. Sie soll eine 
aussagekräftige Fehlermeldung ausgeben, falls negative Werte eingegeben werden.'''

def multiRek(integer, multiplier):
    if integer < 0 or multiplier < 0:
        return "Fehler: Funktion akzeptiert nur natürliche Zahlen (mind. 1 Parameterwert negativ)"
    if multiplier == 0:
        return 0
    
    return integer + multiRek(integer, multiplier - 1)

print(multiRek(5, 10))