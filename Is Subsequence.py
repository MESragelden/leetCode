def isSubsequence(s, t):
        while (len(s) >0):
            try :
                t_index = t.index(s[0])
                s = s[1:]
                t = t[t_index +1:]
            except:
                return False
        return True

print(isSubsequence("abc","ahbgdc"))