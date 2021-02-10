def pascal(line, column):
#als Eingabe die Nummer der Zeile und der Spalte und gibt dann das entsprechende Element zurueck
    if line == 0 or line == 1:
        return 1
    elif line > 1:
        if column == line or column == 0:
            return 1
        else:
            return pascal(line -1 , column) + pascal(line -1, column -1)

print(pascal(35, 8))
