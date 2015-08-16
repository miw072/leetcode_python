class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        if n < 0:
            return ""
        res = []    
        while n > 0:
            res.insert(0, chr(ord('A')+(n-1)%26))
            n = (n-1)/26
        return ''.join(res)    