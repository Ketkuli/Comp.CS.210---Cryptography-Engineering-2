import math
from gcdExtended import gcdExtended

def verifyRSASignature(n:int, e:int, x:int, s:int)->bool:
    """
    Verifies the RSA signature by taking the public key, message and signature
    as parameters. 
    Returns Boolean
    """
    xPrime = (s**e)%n

    if x == xPrime:
        return True
    else:
        return False


def task1():
    n = 9797
    e = 131
    print("\nTask 1:")
    print("Consider the RSA digital signature scheme. Given the public key")
    print("(n=9797, e=131), which of the following signatures are valid?\n")
    
    x=1612
    s=1472
    result = verifyRSASignature(n, e, x, s)
    print(f"x={x} and s={s}: {result}")

    x=1349 
    s=5389
    result = verifyRSASignature(n, e, x, s)
    print(f"x={x} and s={s}: {result}")

    x=3497
    s=5389
    result = verifyRSASignature(n, e, x, s)
    print(f"x={x} and s={s}: {result}\n")
    

def task2():
    n=9797
    e=131
    s=3

    print("Task 2:")
    print("Consider the RSA digital signature scheme. Given the public key\n\
(n = 9797, e = 131), and a signature s = 3, show how Oscar can perform an \n\
existential forgery attack. What is the value of the message x sent by Oscar? ")

    # In existential attack Oscar chooses the signature, in this case s = 3
    # Oscar then computes new message x:
    x = (s**e)%n

    print(f"\nThe new message x for signature s = {s} is: {x}\n")


def calculateElGamalSignature(d:int, p:int, alpha:int, x:int, kE:int)->int:
    kEInverse = pow(kE,-1,p)
    #print(kEInverse)
    r = (alpha**kE)%p
    s = ((x-d*r)*kEInverse)%(p-1)
    print(f"The Elgamal signature for x = {x} and kE = {kE} is r = {r} \
and s = {s}")
    return r,s


def verifyElGamalSignature(p:int, alpha:int, beta:int, x:int, r:int, 
                           s:int) -> bool:
    # calculate t:
    t = ((beta**r)*(r**s))%p

    # verification step:
    if t == (alpha**x)%p:
        return True
    else:
        return False


def task3():
    print("Task 3:")
    print("Consider the Elgamal signature scheme.")
    print("Given Bob’s private key Kpr=(d)=(67), and the corresponding public \
key Kpub=(p,alpha,beta)=(97,23,15).")
    print("Calculate the Elgamal signature (r,s) for the following messages \
x and ephemeral keys kE.\n")
    d, p, alpha, beta = 67, 97, 23, 15

    calculateElGamalSignature(d,p,alpha,17,31)
    calculateElGamalSignature(d,p,alpha,17,49)
    calculateElGamalSignature(d,p,alpha,85,77)

    print("\nMoreover, you receive two alleged messages x1,x2 with their \
corresponding signatures (ri,si) from Bob. \nVerify the signatures and determine \
if they are valid or invalid. \n")
    x1,r1,s1 = 22,37,33
    x2,r2,s2 = 82,13,65

    result = verifyElGamalSignature(p,alpha, beta, x1,r1,s1)
    print(f"The signature for (x1,r1,s1)=({x1},{r1},{s1}) is {result}")

    result = verifyElGamalSignature(p,alpha, beta, x2,r2,s2)
    print(f"The signature for (x2,r2,s2)=({x2},{r2},{s2}) is {result}\n")


def calculateAmountOfEphemeralKeys(p:int)->int:
    # To have eligible Ephemeral key the key must be coprime to p-2
    amount = 0
    for kE in range(2,p-1):
        if math.gcd(kE,p-2) == 1:
            amount += 1
        
    return amount


def task4():
    print("Task 4:")
    print("Consider the Elgamal signature scheme. Given public values p=97, \
α=23, and β=28, and the message x=10\n")
    p, alpha, beta, x = 97,23,28,10
    result = verifyElGamalSignature(p, alpha,beta,x,5,83)
    print(f"Signature (5,83) is {result}")
    result = verifyElGamalSignature(p, alpha,beta,x,41,11)
    print(f"Signature (41,11) is {result}\n")
    print("Moreover, how many valid signatures are there for a message x with \
the parameters given above?")
    amount = calculateAmountOfEphemeralKeys(p)
    print(f"The amount is: {amount}\n")


def existentialAttackElGamal(p:int, alpha:int, beta:int, i:int, j:int)->int:
    # Integers i and j are chosen and deemed valid.
    # Compute the signature (r,s):
    r = ((alpha**i)*(beta**j))%p
    jInverse = pow(j, -1, p-1)
    s = (-r*jInverse)%(p-1)

    # Compute the message:
    x = (s*i)%(p-1)

    return x,r,s


def task5():
    print("Task 5:")
    print("Consider the Elgamal signature scheme. Give the public parameters \
(p=97,α=23,β=15), and the \nchosen values i=3 and j=5. Show how Oscar \
can perform an existential forgery attack. What is the \nvalue of t calculated \
during digital signature verification?")
    p, alpha, beta = 97, 23, 15
    i, j = 3, 5

    x,r,s = existentialAttackElGamal(p, alpha, beta, i, j)

    # Calculating the value t:
    t = ((beta**r)*(r**s))%p
    print(f"The value of t is: {t}\n")


def calcDSAPublicKey(p:int, d:int, alpha:int)->int:
    return (alpha**d)%p


def calcDSASignatures(hash:int, kE:int, p:int, q:int, alpha:int, d:int)->int:
    r = ((alpha**kE)%p)%q
    kEInverse = pow(kE,-1,q)
    s = ((hash + d*r)*kEInverse)%q

    return r,s


def calcDSAVerification(hash:int, s:int, q:int, r:int, alpha:int, 
                        beta:int, p:int)->bool:
    sInverse = pow(s,-1,q)
    w = sInverse%q
    u1 = (w*hash)%q
    u2 = (w*r)%q

    print(f"The auxiliary values are u1 = {u1} and u2 = {u2}")

    v = (((alpha**u1)*(beta**u2))%p)%q

    return v == r%q

    

def task6():
    print("Task 6:")
    print("Consider the DSA digital signature scheme. Given the public \
parameters p=59,q=29,α=3, and Bob’s private \nkey d=23.\n")
    p, q, alpha = 59, 29, 3
    d = 23
    beta = calcDSAPublicKey(p,d,alpha)
    print(f"The public key for Bob is: {beta}\n")

    print("Show the process of signing (Bob) to produce signatures (r,s) and \
verification (Alice) with check \nvalues (u1,u2) for the following hash values \
h(x) and ephemeral keys kE. ")
    hash, kE = 17, 25
    print(f"\nh(x)={hash} and kE={kE}:")
    r,s = calcDSASignatures(hash,kE, p, q, alpha, d)
    print(f"The signatures are r = {r} and s = {s}")
    validity = calcDSAVerification(hash,s, q, r, alpha, beta, p)
    print(f"The calculated signature is: {validity}\n")

    hash, kE = 2, 13
    print(f"\nh(x)={hash} and kE={kE}:")
    r,s = calcDSASignatures(hash,kE, p, q, alpha, d)
    print(f"The signatures are r = {r} and s = {s}")
    validity = calcDSAVerification(hash,s, q, r, alpha, beta, p)
    print(f"The calculated signature is: {validity}\n")

    hash, kE = 21, 8
    print(f"\nh(x)={hash} and kE={kE}:")
    r,s = calcDSASignatures(hash,kE, p, q, alpha, d)
    print(f"The signatures are r = {r} and s = {s}")
    validity = calcDSAVerification(hash,s, q, r, alpha, beta, p)
    print(f"The calculated signature is: {validity}\n")


def printLine():
    print("-"*103)


task1()
printLine()
task2()
printLine()
task3()
printLine()
task4()
printLine()
task5()
printLine()
task6()
