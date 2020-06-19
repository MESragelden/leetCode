def numIslands(grid):
    islands = 0
    length = len(grid)
    width = len(grid[0])
    for i in range (0,length):
        for j in range (0,width):
            if grid[i][j]=="1":
                islands +=checkAdjacent(grid,i,j,length,width)
  #  print(length," ",width)
    return islands

def checkAdjacent(grid,i,j,length,width):
    if (i<0 or i>=length or j<0 or j >=width or grid[i][j]=="0"):
        return 0
    else :
        grid[i][j]="0"
        checkAdjacent(grid,i+1,j,length,width)
        checkAdjacent(grid,i-1,j,length,width)
        checkAdjacent(grid,i,j+1,length,width)
        checkAdjacent(grid,i,j-1,length,width)
        return 1
grid = [["1","1","1","1","0"]
,["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]     


print(numIslands(grid))