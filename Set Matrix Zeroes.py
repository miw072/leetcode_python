# Set Matrix Zeroes
# Mingxuan Wang
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        rows = False
        cols = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        rows = True
                    if j == 0:
                        cols = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        
        if rows:
            for j in range(m):
                matrix[0][j] = 0
                
        if cols:
            for i in range(n):
                matrix[i][0] = 0