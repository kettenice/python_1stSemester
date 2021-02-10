
# 0 ist eine gerade Zahl   
# gerade Zahlen und ungerade Zahlen abwechselnd vorkommen


def even(x):
    
    schalter1 = True
    y = 0
    while y != x:
        y += 1
        if schalter1 == True:
            schalter1 = False
        else:
            schalter1 = True
    return schalter1

def evenRek(x, schalter = True):
        y = 0
        
        if y != x:
            
            if schalter == True:
                schalter = False
            else:
                schalter = True
            return evenRek(x - 1, schalter=schalter) 
        else:
            if schalter == True:
                return True
            else:
                return False


def oddSimple(x):
    y = 0 
    if (((x//2)*2)+1) == x:
        return True
    else:
        return False

def oddRek(x, boolean = True):
    y = 0

    if y != x:
        if boolean == True:
            boolean = False
        else:
            boolean = True
        return oddRek(x - 1, boolean=boolean)
    else:
        if boolean == True:
            return False
        else:
            return True
    

def odd(x):
    
        schalter1 = False
        y = 0
        while y != x:
            y += 1
            if schalter1 == True:
                schalter1 = False
            else:
                schalter1 = True
        return schalter1


b = 57

print("even:", even(b))
print("odd:", odd(b))
print("evenRek:", evenRek(b))
print("oddRek:", oddRek(b))
print("oddSimple:", oddSimple(b))