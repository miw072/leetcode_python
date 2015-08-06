class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
    	 return [(i >> 1) ^ i for i in xrange(2 ** n)] 