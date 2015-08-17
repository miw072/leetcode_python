class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        for i in xrange(32):
        	if (n >> i) & 1 == 1:
        		ret+=1

        return ret		