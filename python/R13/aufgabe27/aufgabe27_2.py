'''
Strings kann man in Python wie Listen behandeln. 
Schreiben Sie eine Funktion die hinter jedes Zeichen 
ein Leerzeichen eingefügt.
'''

def spaceLetters(putput):
    return ' '.join(putput)

bungbung = "bab abiolo"
print(spaceLetters(bungbung))   # b a b a b i o l o
