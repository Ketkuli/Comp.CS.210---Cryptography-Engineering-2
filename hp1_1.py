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

#(1)
# This is the prime from Ex.2
PRIME = 6005491011001

# These are the prime roots of PRIME-1 = 6005491011000 
# I got these from here: https://www.numberempire.com/numberfactorizer.php
P1 = 2
P2 = 3
P3 = 5
P4 = 13
P5 = 17109661

prime_roots = [P1, P2, P3, P4, P5]
s = PRIME - 1
exponents = [ s/root for root in prime_roots]


# Get primes for finding primitive roots:
def prime_list(number):
    primes = []
    for i in range(2, number + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

primes = prime_list(71)


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


# Search for smallest prime root for PRIME
for prime in primes:
    success = 0
    for exp in exponents:
        result = exponentiation(prime, exp, PRIME)
        if result not in prime_roots and result != 1:
            success += 1
        else:
            break
    if success == 5:
        print(f"The smallest primitive root of {PRIME} is {prime}") # is 29.
        break

