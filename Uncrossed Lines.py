def maxUncrossedLines(A, B):
    length_A = len(A)
    length_B = len(B)
    dp = [[0 for i in range(length_B+1)] for j in range(length_A+1)]
    
    for i in range (length_A):
        for j in range(length_B):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else :
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return dp[length_A][length_B]



A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
print(maxUncrossedLines(A,B))

        