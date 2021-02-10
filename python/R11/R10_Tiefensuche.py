
 # 0 = TXL, 1 = CGN, 2 = FRA, 3 = MUC, 
 # 4 = KEL, 5 = STR, 6 = PAD, 7 = SFX

# Name  TXL   CGN     FRA       MUC    KEL STR PAD SFX
# Index  0     1       2         3      4   5   6   7
adj = [[1,2],[0,3],[0,3,4,5],[1,2,6,7],[2],[2],[3],[3]]

def dfs (adj, knoten):
    stack = [knoten]
    counter = 0
    mark = [knoten]
    
    while stack != [] :
        akt = stack[-1]

        if akt not in mark :
            mark.append(akt)

        remove_from_stack = True
        for nachbar in adj[akt] :
            
            if nachbar not in mark:
                counter += 1
                stack.append(nachbar)
                remove_from_stack = False
                break
        if remove_from_stack == True :
            stack.pop()
            
    return counter
    
