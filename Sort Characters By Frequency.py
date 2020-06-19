def frequencySort(s):
        d = dict()
        for c in s :
            if c in d :
                d[c] +=1
            else :
                d[c] =1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}
        new_s = ""
        for ele in d.keys():
            new_s+= ele*d[ele]
        return new_s


print (frequencySort("Aabb"))