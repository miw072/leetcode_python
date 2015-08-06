class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        c = [0 for i in xrange(n+1)]
        c[0] = 1
        c[1] = 1
        for total in xrange(2, n+1):
        	for left in xrange(total):
        		c[total] += c[left] * c[total-1-left]
        return c[n]		