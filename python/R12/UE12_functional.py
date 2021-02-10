def square(x):
          return x*x
def rpk(x):
    if (x==0):
        print("Fehler: Division durch 0")
    else:
        return 1/x

g = lambda f, x: rpk(f(x))

print(g(square, 4))
print(g(square, 4) * 16)