"""
(1) Using your own prime p from Ex2, find a the smallest primitive root of p, 
i.e. such a positive integer that multiplicatively generates all integers 
1,...,p-1. First use a factoring service (e.g. this) to find the primes that 
divide p-1, and then the explanation on this page as a specification for a 
script to calculate the least primitive root.

(2) Assume you have an RSA system with primes p=1009 and q=1013. The message 
m is a positive integer below pq (and the task does not reveal m to you, and 
it is actually not known yet). Encrypting m means raising it to power 3 modulo 
pq. A faster way than using the full modulus pq is to do the exponentiation 
separately with respect to p and q and then combine the results modulo pq. 
This will be your task now. Take

    m3  mod p = u := the three last digits from your student number
    m3  mod q = v := three previous digits.

If either u or v would be 0, make it 1. So, what is the cryptotext c,  
i.e.  m3  mod pq ? The numbers are small enough for you to do trial-and-error, 
but instead apply the Chinese remainder theorem (CRT): Use your extended 
Euclidean algorithm to find x and y that satisfy  xp + yq = 1.  
Then take c = uxp + vyq  mod pq.

Note. These two tasks are not related to each other. Submit your answers, 
the two numbers to Moodle at the proper week under "Hp1". The first task 
requires some scripting. The second task, after using your EEA script, can be 
done on paper. Check its result mod p and mod q, and make sure the result is 
less than pq. There is no calculator provided letting you check either task, 
but if you can afford nearly 1013 multiplications (for each attempt) you can 
simply check the first one and if you bother to find out m from u and v, you 
can also check the final result c.
"""

# (2)
p = 1009
q = 1013

u = 500
v = 194
   

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


# Find x and y for p and q, so that xp + yq = 1:
gcd, x, y= gcdExtended(p, q)

ciphertext = (u*x*p+v*y*q)%(p*q)

print(f"The ciphertext is: {ciphertext}") # is 434064