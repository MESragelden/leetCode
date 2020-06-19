def groupAnagrams(strs):
    d = dict()
    for s in strs:
        abs_str = ''.join(sorted(s))
        #print(abs_str," ",s)
        ret = d.get(abs_str,-1)
        if(ret == -1):
            d[abs_str] = list()
        d[abs_str].append(s)
        #print (ret)

    return list(d.values())




L = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(L))