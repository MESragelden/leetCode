def leftMostColumnWithOne(binaryMatrix):
    if binaryMatrix is None :
        return -1
    length,width = len(binaryMatrix),len(binaryMatrix[0])
    print (length , " ",width)
    if length == 0 and width == 0:
        return -1
        
    i,j = 0,width -1
    print(i," ",j)
    column = -1
    while (i<length and j>=0):
        if (binaryMatrix[i][j] == 1):
            column = j
            j = j-1
           
        else :
            i = i+1
    return column
        
mat = [[0,0,0,1],
       [0,0,1,1],
       [0,1,1,1]]
mat2 = [[0,0],
        [1,1]]
print(leftMostColumnWithOne(mat2))