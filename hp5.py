"""
EC operations

Author: Paavo Peltopihko
Studentnumber: 194500

Task: 
Write functions to do point doubling and adding of two points on the elliptic 
curve  y^2=x^3+ax+b modulo prime p. This will be modified later to replace the 
ordinary integer operations with your functions for big integer operations. 
Submit your code in one file where there are functions addEC(x,y,c) and 
doublEC(x,c),  where the parameters are lists:  x = [x1, x2]  and  y=[y1, y2]  
are the points to add and  c=[p, a, b]  defines the curve. The course staff 
will run your file and check that the functions return a correct result in the 
form of a list  [z1, z2],  where the point at infinity is represented by [0, 0].  
Take the infinity into account also in your input. You can assume that the curve 
is indeed elliptic and the input points are on it.
"""

def gcdExtended(a, b):
    # For finding multiplicative inverse in field:
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y


def addEC(x:list[int,int], y:list[int,int], c:list[int,int, int])->list[int,int]:
    """
    x and y are points on the elliptic curve c that are added together
    returns a point on a curve
    """
    # Checking the input first:
    infinity = [0,0]
    if x == infinity:
        return y
    elif y == infinity:
        return x
    
    # Go to the calculation of the parameters in the elliptic curve:
    else:
        x1,y1 = x
        x2,y2 = y
        p,a,b = c
        # Calculations to get the slope s:
        # Get multiplicative modular inverse for x2-x1:
        gcd, amodp, pmoda = gcdExtended((x2-x1)%p,p)  
        
        # Calculate the slope:
        s = (y2-y1)*amodp%p
        # Check is slope is vertical:
        if s == 0:
            return infinity

        # Calculate new points:
        x3 = (s**2-x1-x2)%p
        y3 = (s*(x1-x3)-y1)%p

        return [x3,y3]


def doublEC(x:list[int,int], c:list[int,int, int])->list[int,int]:
    """
    # x is a point on the curve c that is added with itself
    # returns a point on a curve 
    """
    x1,y1=x

    p,a,b=c

    # Calculations to get the slope s:
    # Get the multiplicative inverse for 2*y1:
    gcd, amodp, pmoda = gcdExtended((2*y1)%p,p)

    # Calculate the slope:
    s = (3*x1**2+a)*amodp%p

    # Calculate new points:
    x3 = (s**2-x1-x1)%p
    y3 = (s*(x1-x3)-y1)%p

    return [x3,y3]


if __name__ == "__main__":
    print("This file is meant to be imported to another .py file to run \
calculations")
