def countSquares(matrix):
        sum = 0
        length = len(matrix)
        width  = len(matrix[0])
        bigg_matrix = [[0]*(width+1) for _ in range(length+1)]
        for i in range (length):
            for j in range (width):
                if (matrix[i][j] == 0):
                    bigg_matrix[i+1][j+1] = 0
                else :
                    bigg_matrix[i+1][j+1] = min(bigg_matrix[i][j+1],bigg_matrix[i+1][j],bigg_matrix[i][j])+1          
                sum += bigg_matrix[i+1][j+1]

        return sum




matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(countSquares(matrix))