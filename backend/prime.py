"""
The Prime script returns a prime number of variable bit sizes.
Methods isProbablePrime and getPrime check to see if the number generated
is prime and returns the prime number respectively.
"""

from random import randrange, getrandbits
from itertools import repeat

#fetched from http://pythonfiddle.com/prime-number-generation/
def isProbablePrime(n, t = 7):
    """Miller-Rabin primality test"""

    def isComposite(a):
        """Check if n is composite"""
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    assert n > 0
    if n < 3:
        return [False, False, True][n]
    elif not n & 1:
        return False
    else:
        s, d = 0, n - 1
        while not d & 1:
            s += 1
            d >>= 1
    for _ in repeat(None, t):
        if isComposite(randrange(2, n)):
            return False
    return True

def getPrime(n):
    """Get a n-bit prime"""
    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p
