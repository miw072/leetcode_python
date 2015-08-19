class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        p, numberPool = 1, [0, 0] + [1 for i in xrange(2, n)]
        for i in xrange(2, n):
            if numberPool[i]:
                p = i
                for k in xrange(2, (n-1)/(p)+1):
                    numberPool[k*p] = 0
        return sum(numberPool)          