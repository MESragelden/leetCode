class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 
        n len(matrix[0])
        height = 0
        ansmatrix = [[0]*(n+1) for _ in range (m+1)]
        for i in range(1,m+1):
            for j in range (1,n+1):
                if matrix[i-1][j-1] == '1':
                    ansmatrix[i][j] = min(ansmatrix[i-1][j],ansmatrix[i][j-1],ansmatrix[i-1][j-1])+1
                    height = max(height,ansmatrix[i][j])
        return height**2
