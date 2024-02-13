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

a + R b + R2 c = s
a + T b + T2 c = u
a + V b + V2 c = w

Solve it for a, b and c, and pick the a as your answer to Moodle. As an exercise 
do this by inverting the coefficient matrix modulo 1009, and use it to multiply  
(s, u, w)  as a column vector. Here is a script for Gauss-Jordan method to 
invert a matrix. "Modularize" it to do the modular inversion. Note that you are 
not looking for a maximal element in the i'th column to be the pivot element, 
but just any (modularly) nonzero element will do. You cannot do division 
directly but you must invert the pivot element modulo 1009 (preferrably with 
your function from Ex1). Otherwise the procedure is the same.
"""