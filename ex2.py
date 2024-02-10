"""
Ex2. Primality testing.

This is also just an exercise and is not scored.

Besides arithmetic, finding prime numbers is essential for traditional PKC. 
Write a script that gives you the next prime larger than a given integer N. 
Do this with following stages:

1. Create a sieve: First make a list smallp of all small primes up to, say, 
31 or 71.
Make the list  sieve = [  p - N % p  for p in smallp].
Start checking if  N+i,  i=0,1,2,...  is a prime (see #2 below). 
Skip each N+i for which  i mod p  for some p  in the list smallp equals the 
corresponding element in sieve. The reasoning for this: if  i % p = p - N % p 
for some prime p, then i=p-N modulo p, or equivalently N+i=0 mod p which means 
that p divides N+i and it is not useful to check it further.

2. Submit the proposed prime N+i to Miller-Rabin test, as in section 7.6.2 in 
the textbook. This is the script for that test, but you must edit three points 
marked with ?? in it. Also include your square & multiply algorithm from Ex1 
and edit the call to match it.  Note: In the textbook Miller-Rabin, the third 
line from line 1.4 should be IF z=p-1.

Test your script against known lists of primes or calculators. Then use it to 
find the next prime that is greater or equal to 6x10^12 +Rx10^6 + 2xR, where R 
equals the six last digits of your student number in reverse order. Check the 
primality of your result against the calculator. You will need this prime in 
the two following tasks.
"""

def prime_list(number):
    primes = []
    for i in range(2, number + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

PRIMES = prime_list(71)


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


def miller_rabin(pp, s):
    ''' Test a proposed prime pp>3 s times 
    (to make probability sufficient, check textbook table 7.2 or other sources for s)

    This script has the same symbols as in the textbook but the control flow
    is organized in a slightly different way. Note also that the textbook has a typo:
    The third line from line 1.4 should be IF z=p-1.
    '''
    from random import randrange    # like randint but works like range()
    u = 0              # exponent of highest power of 2 dividing pp-1
    r = pp - 1
    while r % 2 == 0:   # as long as r is even
        u += 1
        r = (pp-1)/(2**u)
                      # Now pp = 2^u * r
    for _ in range(s):      # k rounds with a dummy index _
        a = randrange(2, pp - 1)  # the highest choice is pp-2
        z = exponentiation(a, r, pp)      # z = (a**r)%pp
        if z == 1 or z == pp-1:
            continue                # pick new 'a' (if there are still rounds)
        for _ in range(u - 1):      # u-1 squarings
            z = z**2%pp
            if z == pp - 1:          
                break           # stop squaring, ... pick new 'a'
        else:               # this associates with the last 'for', and
            return False    # ... leads here if the loop did not 'break' 
    return True

def find_next_prime(N):
    sieve = [p - N % p for p in PRIMES]
    
    not_prime = True
    i = 0
    while not_prime:
        for index in range(len(PRIMES)):
            p = PRIMES[index]
            if i % p != sieve[index]:
                is_prime = miller_rabin(N+i, 11)
                if is_prime == True:
                    return N+i
                else: 
                    continue
        i += 1    
        

def reverse_numbers(number):
    """
    Script to reverse given number
    """
    reverse_number = 0
    while number != 0:
        digit = number % 10
        reverse_number = reverse_number*10+digit
        number //= 10
    return reverse_number

#print(reverse_numbers(194500))
#num = 194500
#print(int(str(num)[::-1]))

R = reverse_numbers(194500)

N_to_look_for = 6*(10**12)+R*(10**6)+2*R
print(find_next_prime(N_to_look_for))



