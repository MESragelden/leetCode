def firstUniqChar(s):
    import sys
    d = dict()
    for i in range (0,len(s)):
        if s[i] not in d :
            d[s[i]]= [1,i]
        else :
            d[s[i]]=[d[s[i]][0]+1,d[s[i]][1]]
    minIndex = sys.maxsize
    for ele in d.values() :
        if ele[0] == 1:
            if ele[1]< minIndex:
                minIndex = ele[1]
    return minIndex

print(firstUniqChar("loveleetcode"))
    
        