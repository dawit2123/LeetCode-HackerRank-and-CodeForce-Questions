# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def euler(num: int) -> int:
            p, res = 3, num
            if not num&1:
                res >>= 1
                while not num&1:    num >>= 1
            while num >= p*p:
                if not num%p:
                    res = res//p*(p-1)
                    while not num%p:    num //= p
                p += 2
            if num > 1:
                res = res//num*(num-1)
            return res

        if gcd(power,modulo) == 1:
            h, pp, inv = 0, 1, pow(power, euler(modulo)-1, modulo)
            for i in range(k):
                h = (h + pp * (ord(s[i])-96)) % modulo
                pp = pp * power % modulo
            for i,c in enumerate(s[k:]):
                if h == hashValue:  return s[i:i+k]
                h = (h+(ord(c)-96)*pp-ord(s[i])+96) % modulo
                h = h * inv % modulo
            return s[-k:]
        else:
            res, n, h, pp = len(s)-k, len(s), 0, 1
            for i in range(-k,0):
                h = (h + pp * (ord(s[i])-96)) % modulo
                pp = pp * power % modulo
            for i in range(n-k-1, -1, -1):
                h = (h*power-(ord(s[i+k])-96)*pp+ord(s[i])-96) % modulo
                if h == hashValue:  res = i
            return s[res:res+k]