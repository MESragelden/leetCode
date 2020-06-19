def stringShift(s,shift):
    right = left = 0
    for ele in shift:
        if ele[0] == 1:
            right += ele[1]
        else :
            left += ele[1]
    #print (left , " ", right)
    diff = abs(right - left)%len(s)
    if (right > left):
        return (s[-diff:]+s[:-diff])
    elif(left > right):
        return(s[diff:]+s[:diff])

    else :
        return s




s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]


s1 = "abc"
shift1 = [[0,1],[1,2]]

s2 = "mecsk"
shift2 = [[1,4],[0,5],[0,4],[1,1],[1,5]]
s3 = "xqgwkiqpif"
shift3 = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
print(stringShift(s3,shift3))