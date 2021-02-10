

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print(a, b, c)
        c.append(a.pop())
        hanoi(n-1, b, a, c)

n=3
x, y, z = list(range(n, 0, -1)), [], []
hanoi(n, x, y, z)
print (z)
'''
[3, 2, 1] []c []b
[3, 2] [1] []
[1] [3] [2]
[3] [2, 1] []
[2, 1] [3] []
[2] [1] [3]
[1] [] [3, 2]
[3, 2, 1]'''