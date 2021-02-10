class Stack:
    def __init__(self, collectable=[]):
        self.S = collectable

    def __str__(self):
        return str(self.S)
    def __repr__(self):
        return str(self.__str__())

    def push(self, new):
        self.S.append(new)
        return len(self.S)

    def top(self):
        return self.S[-1]

    def pop(self):
        latestElement = self.S[-1]
        del self.S[-1]
        return latestElement

    def size(self):
        return print("Size of Stack is", len(self.S))

    def flip(self):
        self.tempS = []
        for i in range(len(self.S) - 1, -1, -1):
            self.tempS.append(self.S[i])
        self.S = self.tempS

    def isEmpty(self):
        if self.S == []:
            return True
        else:
            return False



        


