from hp5 import doublEC, addEC
from ECDLP import solveECDLP

def isEllipticCurve(a:int,b:int,p:int)->bool:
    if a == 0 or b == 0:
        return False
    elif (4*a**3+27*b**2)%p==0:
        return False
    else:
        return True
          

def doubleAndAdd(P:list[int,int], k:int, c:list[int,int,int])->list[int,int]:
    """
    param:
    P = [x1,y1]
    k = multiplier aka private key
    c = [p,a,b]

    Returns Q from Q = kP mod p
    """

    T = P
    i = 1 # Keeps the round "number" in memory

    while i < k:
        # This is to check if infinity:
        if T == [0,0]:
            T = P
        # This is for case when it is P+P:
        elif T == P:
            T = doublEC(T,c)
        # This is for all other cases:
        else:
            T = addEC(T,P,c)          
        i += 1

    return T


def ECDH(P:list[int,int], c:list[int,int,int], ska:int, skb:int)->list[int,int]:
    A = doubleAndAdd(P,ska,c)
    B = doubleAndAdd(P,skb,c)

    Tab = doubleAndAdd(B,ska,c)
    Tba = doubleAndAdd(A,skb,c)

    if Tab != Tba:
        print("Something fishy in your calculations")
        return [0,0]
    else:
        return Tab

def main():
    print("\nQuestion 1:")
    print("The equation y^2 = x^3 + 3x + 7 mod 23 is elliptic curve:")
    print(isEllipticCurve(3,7,23))
    print("The equation y^2 = x^3 + 11x + 7 mod 23 is elliptic curve:")
    print(isEllipticCurve(11,7,23))
    print("The equation y^2 = x^3 + 8x + 20 mod 23 is elliptic curve:")
    print(isEllipticCurve(8,20,23))
    print("The equation y^2 = x^3 + 17x + 20 mod 23 is elliptic curve:")
    print(isEllipticCurve(17,20,23))

    print("\nQuestion 2:")
    print("Take the curve E with equation y^2 = ^3 + 7x + 7 mod 23")

    print("Compute 2P, where P=(8,0)")
    print(doublEC([8,0],[23,7,7]))
    
    print("Compute 2P, where P=(2,12)")
    print(doublEC([2,12],[23,7,7]))

    print("\nQuestion 3:")
    print("Take the curve E with equation y^2 = x^3 + 7x + 7 mod23")
    print("Compute P+Q where P=(8,0) and Q=(17,18)")
    print(addEC([8,0],[17,18],[23,7,7]))

    print("Compute P+Q where P=(17,5) and Q=(17,18)")
    print(addEC([17,5],[17,18],[23,7,7]))

    print("Compute P+Q where P=(17,18) and Q=(17,18)")
    print(addEC([17,18],[17,18],[23,7,7]))

    print("\nQuestion 4: ")
    print("Given points P=(2,12) and Q=(8,0) on the curve with equation\
y2=x3+7x+7mod23,\nfind the smallest positive k that Q=kP holds.\
In other words solve the discrete logarithm problem.")
    print(f"k = {solveECDLP([2,12],[8,0],[23,7,7])}")


    print("\nQuestion 5:")
    print("Given the curve E with equation y^2 = x^3 + 7x + 7 mod 23, and the point\
 P=(2,12) on the curve E. \nCompute 17P and enter the coordinates below.\n\
Hint: use the double-and-add algorithm. ")
    print(f"17P = {doubleAndAdd([2,12], 17, [23,7,7])}")

    print("\nQuestion 6:")
    print("Given the elliptic curve E with equation y2=x3+7x+7mod23, and the generator point P=(2,12) on the curve E.")
    print("Compute the ECDH shared secret between Alice and Bob using the secret keys ska=17 and skb=13, respectively.")
    print("Enter the coordinates below. ")
    result = ECDH([2,12], [23,7,7], 17, 13)
    print(f"x = {result[0]}, y = {result[1]}")

main()