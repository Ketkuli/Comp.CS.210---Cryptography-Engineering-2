"""
Assume f is a polynomial a+bx+cx2 over GF(1009) and f(10+r)=s, f(20+t)=u, 
f(30+v)=w, where the values r,...,w are decimal digits taken from your student 
number, which is ***rstuvw. (If your s, u and w are all equal, add 1 to w.) Your 
task is to find f(0), that is, the constant term a. You can imagine that the 
value a is the secret that you have hidden in several places as the values of 
the polynomial f(x), for the particular values of x (those three or more). You 
had picked random b and c (≠0) for the polynomial to calculate the values f(x), 
but then you deleted a, b and c. Now the adversary and you, too, must get a 
hold of at least three of the values s, u and w (...) to reconstruct the secret 
a. (The normal assumption is that the x's are known, and for simplicity they 
would be just 1, 2, 3,.... Now, the x's are just a little strange to make the 
task different for all, but the adversary is supposed to know r, t, and v.)

One of the videos for this week explains this method of sharing a secret 
(and Wikipedia continues) and uses Lagrangian interpolation to find the secret. 
You need not use that method here. Instead just write a system of equations 
(as is done in the follow-up video), with obvious meanings for R, T and V:

a + R b + R^2 c = s
a + T b + T^2 c = u
a + V b + V^2 c = w

Solve it for a, b and c, and pick the a as your answer to Moodle. As an exercise 
do this by inverting the coefficient matrix modulo 1009, and use it to multiply  
(s, u, w)  as a column vector. Here is a script for Gauss-Jordan method to 
invert a matrix. "Modularize" it to do the modular inversion. Note that you are 
not looking for a maximal element in the i'th column to be the pivot element, 
but just any (modularly) nonzero element will do. You cannot do division 
directly but you must invert the pivot element modulo 1009 (preferrably with 
your function from Ex1). Otherwise the procedure is the same.
"""

primeField = 1009

r = 1
s = 9
t = 4
u = 5
v = 0
w = 0

R = 10 + r
T = 20 + t
V = 30 + v 

# a + R*b + (R**2)*c = s
# a + T*b + (T**2)*c = u
# a + V*b + (V**2)*c = w

A = [[1, R, R**2],
     [1, T, T**2],
     [1, V, V**2]]

b = [[s],
     [u],
     [w]]

# To solve the values of a, b and c we know that coefficient matrix calculus is
# following: Ax = b where A is the coefficients, x is a column of unknown 
# variables and the b is the solution column. 

# This gives us the knowledge that x equals the inverse of A multiplied with b.
# Import gauss jordan to calculate inverse:
from GaussJordan import modularInvert

# Multiply square matrix a and column vector b.
def multiply(a,b):
    n = len(a)
    res = [[0],[0],[0]]
    for i in range(n):
        for j in range(n):
            res[i][0] += a[i][j] * b[j][0]
    return res

def isTrue(solution):
    a = solution[0][0]
    b = solution[1][0]
    c = solution[2][0]
    #a = 818
    #b = 49
    #c = 706

    if (a+b*R+c*R**2)%primeField == s and (a+b*T+c*T**2)%primeField == u  and (a+b*V+c*V**2)%primeField == w:
        return True
    else:
        return False 


print(A)

inverse = modularInvert(A, primeField)
solution = multiply(inverse, b)

print(inverse)
print(solution)

print(f"The solution is {isTrue(solution)}")



