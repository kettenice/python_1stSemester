def fiboRek(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    return fiboRek(x-1) + fiboRek(x-2)

#print(fiboRek(7))

def fiboIte(x):
    fib0, fib1 = 1, 1
    for x in range(0, x+1):
       
        if x > 1:
            temp = fib1
            fib1 = fib0 + fib1
            fib0 = temp
    return fib1

#print(fiboIte(7))



