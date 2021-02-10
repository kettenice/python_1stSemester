import profile
import random

L = []
for o in range(10,000):
    L.append(random.randint(1, 100))
L.sort()

sum1 = 31
def f1(list, sum):
    for i in list:
        for e in list:
            if (e + i) == sum :
                print( str(e) + " + " + str(i) + " = " + str(sum) )
    print("No two elements sum up to " + str(sum))
def f2(list, sum):
    i = 0
    j = 1
    k = False
    while (list[len(list)-j] + list[i]) != sum:
        if (j > list[len(list) - 1]) or (i > list[len(list) - 1]):
            print("No two elements sum up to " + str(sum))
            k = True
            break

        if (list[len(list)-j] + list[i]) > sum:
            j = j + 1
        elif (list[len(list)-j] + list[i]) < sum:
            i = i + 1
    if k == False:
        print( str(list[len(list)-j]) + " + " + str(list[i]) + " = " + str(sum))
#f1(L, sum1)
#f2(L, sum1)


