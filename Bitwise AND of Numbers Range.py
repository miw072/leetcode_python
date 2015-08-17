class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        mask = 2**31-1
        while m&mask != n&mask: mask<<=1
        return mask&m