class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        A = [0 for i in xrange(rowIndex+1)]
        A[0] = 1
        for i in xrange(1, rowIndex+1):
        	for j in xrange(i, 0, -1):
        		A[j] += A[j-1]
        return A		