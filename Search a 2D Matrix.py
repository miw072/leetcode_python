# Search a 2D Matrix 
# Mingxuan Wang
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows * cols - 1

        while start+1 < end:
        	mid = (start+end)/2
        	cell = matrix[mid/cols][mid%cols]

        	if cell == target:
        		return True
        	elif cell < target:
        		start = mid + 1
        	else:
        		end = mid - 1
        return False		