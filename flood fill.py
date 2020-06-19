def floodFill(image, sr, sc, newColor):
    def checkneighbours(i,j,L):
        if (i >= length or i < 0  ):
            return
        if (j >= width or j < 0 ):
            return
        if (image[i][j] != color):
            return 
        else :
            if (i,j) in L:
                return
            image[i][j] = newColor
            L.append((i,j))
            checkneighbours(i,j+1,L)
            checkneighbours(i,j-1,L)
            checkneighbours(i+1,j,L)
            checkneighbours(i-1,j,L)

    if image == None:
        return  
    length = len(image)
    width = len(image[0])
    L = []
    color = image[sr][sc]
    checkneighbours(sr,sc,L)
    
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = image[sr][sc]
newColor = 2
print(floodFill(image,sr,sc,newColor))
         