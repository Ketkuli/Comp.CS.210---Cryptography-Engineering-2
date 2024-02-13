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

from numpy import invert, transpose

test = [300, 
        500, 
        600, 
        700]
testSum = 1200

givenPublicKey = [7035238348546, 7589484607469, 5006080475994, 5701080243151, 
                  7093112614563, 5419139272946, 6739805882947, 4308219917231, 
                  7666668559292, 7855284573687, 4931746167290, 7329232672795, 
                  4709097576863, 6623899022169, 4407434511793, 5267629531588, 
                  7930493753592, 7651225087488, 7406118667681, 4960648457133, 
                  7180236876183, 4352772048223, 6546713299361, 4353662854347]


subsetSum = 60615973367597

# Stuff provided by teacher begins:

# To get the inverse W of a square matrix M, call: W = invert(M)
from GaussJordan import *

# Inner product (dot product) of vectors a and b.
def dotp(a,b):
    return sum(x*y for x, y in zip(a, b))

# Transpose of matrix a.
def transpose(a):
    return [[row[col] for row in a] for col in range(len(a[0]))]

# Multiply square matrices a and b.
def multiply(a,b):
    n = len(a)
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res

# The only operation inside Gram-Schmidt:
# subtract from v the projection of v onto u.
def project_and_subtract(u, v):
    udotv_per_udotu = dotp(u, v) / dotp(u, u)
    return [ (v_i-udotv_per_udotu*u_i)  for v_i, u_i in zip(v, u) ]

# Gram-Schmidt orthogonalization for a list of vectors
def GS(vectors):
    ulist = []
    for v in vectors:
        for u in ulist:
            v = project_and_subtract( u, v )  # project v onto u
        ulist.append(v)
    return ulist

# LLL-reduction
def LLL(basis, delta=0.75):
    n = len(basis)
    B = GS(basis)
    Bstar = multiply(B, invert(multiply(transpose(B), B)) )
    def mu(i,j):
        return dotp(basis[i], Bstar[j])
    k = 1
    while k < n:
        for j in range(k-1, -1, -1):
            mu_kj = mu(k,j)
            if abs(mu_kj) > 0.5:
                basis[k] = [basis[k][i] - round(mu_kj)*basis[j][i] for i in range(n)]
                B = GS(basis)
                Bstar = multiply(B, invert(multiply(transpose(B), B)))
        if dotp(B[k],B[k])**2 >= (delta - mu(k, k-1)**2)*dotp(B[k-1],B[k-1])**2:
            k += 1
        else:
            basis[k], basis[k-1] = basis[k-1], basis[k]
            B = GS(basis)
            Bstar = multiply(B, invert(multiply(transpose(B), B)) )
            k = max(k-1, 1)
    return basis

# Stuff provided by teacher ends.

# Create basis aka NxN identity matrix where last column is the values and the 
# sum which is needed to solve:

def createBasis(values, sum):
    # Create identity matrix
    n = len(values)
    basis = [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)]

    # append values in the values as last column to the identity matrix:
    for i in range(n):
        basis[i].append(values[i])

    #Create last row:
    lastRow = [0]*n
    lastRow.append(-1*sum)

    basis.append(lastRow)
    return basis


def checkResult(binaryVector,publicKey, sum):
    checkSum = 0
    for index in range(len(binaryVector)-1):
        if binaryVector[index] == 1:
            checkSum += publicKey[index]

    if checkSum == sum:
        return True
    else:
        return False


def main():
    #basis = createBasis(test,testSum)
    basis = createBasis(givenPublicKey, subsetSum)
    print("This is the original matrix:")
    for row in basis:
        print(row)

    print("\nThis is the solution and the solution is on the top line:")
    solution = LLL(basis)
    for row in solution:
        print(row)

    #result = checkResult(solution[0], test, testSum)
    result = checkResult(solution[0], givenPublicKey, subsetSum)
    print(f"\nThe solution is {result}")



main()