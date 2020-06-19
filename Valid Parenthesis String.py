def checkValidString(s):
    size = len(s)
    astrs = 0
    astrs_lst_pos =[]
    open_par = 0
    open_par_lst_pos= [] 
    for i in range (0,size) :
        if s[i] == '(':
            open_par +=1    
            open_par_lst_pos.append(i)
        elif s[i] == "*":
            astrs +=1
            astrs_lst_pos.append(i)
        else :
            if open_par>0:
                open_par -=1
                open_par_lst_pos.pop()
            elif astrs >0:
                astrs -= 1
                astrs_lst_pos.pop()
            else :
                return False
    if (open_par > astrs):                
        return False
    else :
        while(len(open_par_lst_pos)>0):
            if(open_par_lst_pos[-1]>astrs_lst_pos[-1]):
                return False
            open_par_lst_pos.pop()
            astrs_lst_pos.pop()
        return True

s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
l = "(*()"
print(checkValidString(s))



def test (s):
    op= 0
    clo = 0
    ast = 0
    for c in s :
        if c =="(":
            op += 1
        elif c =="*":
            ast += 1
        else:
            clo += 1
    print("open = ",op," Close = ",clo,"  ast = ",ast)
#test(s)


        