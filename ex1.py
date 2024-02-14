'''
Ex1. EEA, Extended Euclidean Algorithm. Square & multiply.

This is a warm-up exercise: Implement the two indispensable algorithms for 
PKC: modular inversion and exponentiation. The textbook will give you details 
on Extended Euclidean Algorithm (EEA) to do the former and on square & multiply 
to do the latter. Have the EEA output all three values: the gcd and the 
multipliers (m and n) in the Bezout's identity (where gcd( a, b ) = m a + n b ).

Make the scripts functions that you can call in later exercises. Of course 
Python's arithmetic allows you not only to check but calculate directly with 
function pow(base, exponent, modulus). There are also many online calculators 
available. A very powerful entire system is sagemath.org, that may prove useful 
later on. Tanja Lange at TU Eindhoven has a video showing how to use Sage, 
covering basics of finite fields and elliptic curves. You will be fine without 
Sage, though.

Link to the video: https://www.youtube-nocookie.com/embed/92qhT8BAdRk
'''

def exponentiation(base, exp, mod):
    if (exp == 0):
        return 1
    if (exp == 1):
        return base % mod
    
    t = exponentiation(base, int(exp / 2), mod)
    t = (t * t) % mod
     
    # if exponent is
    # even value
    if (exp % 2 == 0):
        return t
         
    # if exponent is
    # odd value
    else:
        return ((base % mod) * t) % mod


def gcdExtended(a, b):
 
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y


p = 1009
q = 1013

print(gcdExtended(p,q))