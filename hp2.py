"""
Hp2. Use LLL against a subset sum.

Here is a fixed public key for a knapsack cryptosystem with N=24 elements. 
Ask your personal subset sum from the calculator, and then find the addends 
using the Lenstra-Lenstra-Lovász algorithm (LLL, linked below). The LLL is used 
for lattice reduction which means that it tries to find short vectors that span 
the same lattice as a given set of vectors. You will feed to LLL such vectors 
that are made very long by including one knapsack element in each, and the 
subset sum to be solved in the last vector.

You will create the vectors more directly in your code, but conceptually you 
first make an NxN identity matrix and then append the knapsack as a new 
rightmost column. Then you append a new bottom row of all zeros and change the 
rightmost element to be the subset sum. Put a minus sign in front of it to get 
positive results.

The basis you just created on the rows of the matrix is very much skewed into 
the last dimension, like in this example:
[[1, 0, 0, 0,  300],
[ 0, 1, 0, 0,  500], *
[ 0, 0, 1, 0,  600],
[ 0, 0, 0, 1,  700], *
[ 0, 0, 0, 0, -1200]] *

but you know that with a suitable linear combination of the rows you will get a 
very neat vector, consisting of just zeros and ones. Summing the rows marked 
with a * you'll get the vector [ 0,1,0,1, 0]., which gives you the solution 
[ 0,1,0,1 ] to this subset sum problem: "Which elements of [300, 500, 600, 700] 
were added to give 1200?"

The LLL algorithm here will give you a basis with shorter vectors spanning the 
same lattice as the rows of your matrix. Chances are good that among the new 
basis vectors you have the actually shortest one, corresponding to the solution. 
You must study the LLL for instance from the Wikipedia to complete the four 
points where a ???? appears. Those three points that compute B* in various 
contexts are identical.

From the example above, the LLL algorithm gives this basis, where the solution 
is on the first row:

[[0,  1,  0, 1, 0 ]
[ 0,  0, -2, 0, 0 ]
[-2,  0,  1, 0, 0 ]
[ 1, -2,  0, 1, 0 ]
[ 0,  1, -1, 0, -100]]

The other rows are also linear combinations of the original base, but they are 
not useful for the solution. For instance the second row [0, 0, -2, 0, 0] 
results from combining the vectors with coefficients [0, 0, -2, 0, x], where the 
beginning is easy to see from the diagonal part of the original matrix, and then 
x can be seen to be -1. Similarly the last row means the coefficients 
[0, 1, -1, 0, 0]. Try this and other small examples before getting into the real 
task of Hp2.

There are many explanations of the LLL algorithm, like here with pedagogic 
discussion of the meaning. This has a short example of another usage. And you 
will encounter more on the post-quantum crypto course. Using LLL against the 
knapsack is not always successful, and while it uses floating point arithmetic 
in its orthogonalization procedure, there will be size limits in plain Python. 
This is why you are not likely to succeed if you test LLL directly against your 
knapsack from Ex3.

See short lecture notes by Chris Peikert on breaking the knapsack with lattice 
reduction. There you'll see the base matrix in transposed form and the last row 
multiplied by a large constant.
"""