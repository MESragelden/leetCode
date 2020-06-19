def hIndex(citations):
    if (len(citations) == 1):
        if citations[0] == 1:
            return 1 
        else :
            return 0
    i = 0
    for ele in reversed(citations):
        if i >= ele:
            return i
        i +=1 
    return i-1
print(hIndex([100]))