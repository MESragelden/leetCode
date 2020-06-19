def solve(board):

    def checkBoundary(board,dic):
        length,width = len(board),len(board[0])
        for j in range (width):
            if board[0][j] == 'O' and (0,j) not in dic:
                dic[(0,j)] = False
                checkAround(board,0,j,dic) 
        for i in range(length):
            if board[i][0] == 'O' and (i,0) not in dic:
                dic[(i,0)] = False
                checkAround(board,i,0,dic) 
        for j in range (width):
            if board[length-1][j] == 'O' and (length-1,j) not in dic:
                dic[(length-1,j)] = False
                checkAround(board,length-1,j,dic) 
        for i in range(length):
            if board[i][width-1] == 'O' and (i,width-1) not in dic:
                dic[(i,width-1)] = False
                checkAround(board,i,width-1,dic) 

    def checkAround(board,i,j,dic):
        if (i,j) in dic :
            return dic[(i,j)]
        try:
            if board[i][j] == 'X':
                return 
            else :
                dic[(i,j)] = False
                checkAround(board,i,j+1,dic)
                checkAround(board,i,j-1,dic)
                checkAround(board,i+1,j,dic)
                checkAround(board,i-1,j,dic)
        except:
            print(i,j)

    dic = dict()
    checkBoundary(board,dic)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O' and (i,j) not in dic:
                board[i][j] = 'X'
    print(board)


board2 = [["X","X","X","X"],
        ["X","O","X","X"],
        ["X","O","O","X"],
        ["X","O","X","X"]]
board = [["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]

print(solve(board2))