from hp5 import doublEC, addEC

def solveECDLP(P:list[int,int], Q:list[int,int], c:list[int,int,int])->int:
    """
    param:
    x = [x1,y1]
    target = [x2,y2]
    c = [p,a,b]

    Returns k from Q = kP mod p
    """
    result = P
    k = 1
    
    while result != Q:
        # This is to check if infinity:
        if result == [0,0]:
            result = P
        # This is for case when it is P+P:
        elif result == P:
            result = doublEC(result,c)
        # This is for all other cases:
        else:
            result = addEC(result,P,c)          
        k += 1
        #print(result)

        if k > 100:
            break
    return k


P = [2,12]
Q = [8,0]
C = [23,7,7]

k = solveECDLP(P,Q,C)
#print(k)
