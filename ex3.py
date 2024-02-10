"""
Create a superincreasing list A of 40 integers in the following way:

A[0]=2,

when i=1,...,6:  A[ i ] = sum( A[ j ], j=0,...,i-1 ) + 1 + the i'th digit from 
the end of your student number.

when i=7,...,39: A[ i ] = sum( A[ j ], j=0,...,i-1 ) + 1

Let W = 54321*108 + six last digits of your student number. Using your own 
prime p from Ex2, multiply each element in the sequence with W modulo p to make 
list B.

Submit your student number to the calculator to obtain a random subset sum of B 
(= sum of elements in a subset of B). Find the addends. Check your answer 
yourself.


What you did here is that you created a small knapsack cryptosystem of the 
original Merkle-Hellman type, with B as the public key, received an encrypted 
message from the calculator, and decrypted it, (apparently) by using the 
trapdoor (p and W, apparently after inverting W mod p) to convert the subset sum 
to be a subset sum of A. That subset sum was easy to solve because of the 
superincreasing structure of A. The task was comparable to converting a decimal 
number to binary by subtracting the highest possible power of 2 in succession. 
Of course, you already followed good programming practice by first testing your 
decryption with a small superincreasing knapsack A and a random binary message 
vector  M=[randint(0,1) for _ in range(len(A))].  The subset sum is easy to make 
by  sum( [M[i]*A[i] for i in range(len(A))]).

You will next break a knapsack cryptosystem by using a lattice reduction 
algorithm, without knowing the trapdoor. You can try the approach of Hp2 also 
with this Ex3 but you probably won't get good results—if any. Remember that here 
in Ex3 you are the legitimate owner of the knapsack.
"""