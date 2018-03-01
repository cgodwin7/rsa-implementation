"""
KeyCreator sets up keys via the extended euclidean algorithm
and serves both public and private 512 bit keypairs.
"""

from backend import prime

class KeyCreator(object):

    def __init__(self):
        self.p = prime.getPrime(1024)
        self.q = prime.getPrime(1024)
        self.n = self.p * self.q
        self.sigN = (self.p-1)*(self.q-1)
        self.e = prime.getPrime(512)
        self.d = self.mod_inverse(self.e, self.sigN)

    def fetchPrivKey(self):
        return self.e, self.n

    def fetchPubKey(self):
        return self.d, self.n

    #fetched from WikiBooks Python iterative algorithm
    def ext_euc_algo(self, b, n):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
            q, b, n = b // n, n, b % n
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return  b, x0, y0

    #fetched from WikiBooks Python modular inverse algorithm
    def mod_inverse(self, b, n):
        g, x, _ = self.ext_euc_algo(b, n)
        if g == 1:
            return x % n



