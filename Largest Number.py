class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(i) for i in nums]
        num.sort(cmp= lambda x,y: (x+y < y+x) - (x+y > y+x))
        return ''.join(num).lstrip('0') or '0'