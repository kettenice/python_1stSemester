
class houseBsp:
    m2 = 0
    nor = 0
    ppm = 0

bauhaus = houseBsp()
bauhaus.m2 = 20
bauhaus.nor = 30
bauhaus.ppm = 60

#print(bauhaus, bauhaus.m2, bauhaus.nor, bauhaus.ppm)
import functools
@functools.total_ordering
class house:
    def __init__(self, size=0, rooms=0, price=0):
        self.m2 = size
        self.nor = rooms
        self.ppm = price
    def calcPrice(self):
        p = int(self.m2 * self.ppm)
        return p
    def setPrice(self, totalPrice):
        self.ppm = totalPrice / self.m2
        return self.ppm
    def printDescription(self):
        return "\nGröße: " + str(self.m2) + "m^2" + "\nRaumanzahl: " + str(self.nor)+ "\nPreis pro m^2: " + str(self.ppm) + "€"
    def __str__(self):
        return self.printDescription()
    def __eq__(self, other):
        return self.calcPrice() == other.calcPrice()
    def __lt__(self, other):
        return self.calcPrice() < other.calcPrice()

        
         
    
         


h1 = house(50, 3, 8)
h2 = house(26, 1, 6 )
m = h2.calcPrice
print(h1 != h2)
print(h2 > h1)

