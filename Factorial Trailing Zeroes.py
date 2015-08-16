class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        res = 0
        while n:
        	n /= 5
        	res += n
        return res	