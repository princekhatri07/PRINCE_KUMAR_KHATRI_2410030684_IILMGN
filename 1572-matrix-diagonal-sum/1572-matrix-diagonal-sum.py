class Solution(object):
    def diagonalSum(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        sum = 0

        if len(mat) == 1:
            return mat[0][0]
        
        for i in range(0,rows):
            for j in range(0,cols):
                if (i == j) or (i+j == rows -1) :
                    sum = sum+ mat[i][j]
        return sum
                


      
        