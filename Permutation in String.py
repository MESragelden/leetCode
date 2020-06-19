def checkInclusion(s1,s2):
    from collections import Counter
    s1_counter = Counter(s1)
    print (s1_counter)
    s2_counter = Counter()
    len_s1,len_s2 = len(s1),len(s2)
    for i in range(len_s2):
        s2_counter[s2[i]] +=1
        if i >= len_s1:
            if s2_counter[s2[i-len_s1]] == 1:
                del s2_counter[s2[i-len_s1]]
            else :
                 s2_counter[s2[i-len_s1]] -=1
        if s2_counter == s1_counter:
            return True
    return False
s1= "ab"
s2 = "eidboaoo"
print(checkInclusion(s1,s2))