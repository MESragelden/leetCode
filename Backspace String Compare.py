'''def backspaceCompare(S,T):
    s_tr = S.split("#")
    t_tr = T.split("#")
    for i in range (0,len(s_tr)-1):
        s_tr[i]=s_tr[i][:-1]
    for i in range (0,len(t_tr)-1):
        t_tr[i]=t_tr[i][:-1]
    s =""
    t = ""
    return(s.join(s_tr)==t.join(t_tr))

'''
def backspaceCompare(S,T):
    s_stk = []
    t_stk = []
    for c in S :
        if c.isalpha():
            s_stk.append(c)
        elif ((not c.isalpha())and len(s_stk) >0):
            s_stk.pop()
    for c in T:
        if c.isalpha():
            t_stk.append(c)
        elif ((not c.isalpha())and len(t_stk) >0):
            t_stk.pop()        
    s =""
    t = ""
    return(s.join(s_stk)==t.join(t_stk))        
#S = "xywrrmp" -->True
#T = "xywrrmu#p"
S = "ab#c"
# --->True
T = "ad#c"
#S = "ab##"
#T = "c#d#"
print(backspaceCompare(S,T))