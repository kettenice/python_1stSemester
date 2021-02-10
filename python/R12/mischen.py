from class_stack import Stack

def mischen(A, B):
    A = Stack(A)
    B = Stack(B)
    C = Stack([])
    while A.S != [] and B.S != []:
    
        if len(A.S) == 1:
            topA = A.S[0]
        else:
            topA = A.top()          
        if len(B.S) == 1:
            topB = B.S[0]
        else:
            topB = B.top()
         
        if topA > topB:
            C.push(B.pop())
        elif topA < topB:
            C.push(A.pop())
        elif topA == topB:
            C.push(A.pop())
            C.push(B.pop())
        print(topA, topB)
    if A.S == []:
        while B.S != []:
            C.push(B.pop())
            print(C)
    elif B.S == []:
        while A.S != []:
            C.push(A.pop())
            print(C)
    return C
