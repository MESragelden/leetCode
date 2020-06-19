def removeKdigits(num, k):
        length = len(num)
        if(length == 0 )or (k>=length):
            return "0"
        st = []
        st.append(num[0])
        remove = k
        for ele in num[1:]:
            while st and st[-1]>ele and remove >0 :
                st.pop()
                remove -=1
            st.append(ele)        
        ans = "".join(st[:len(num)-k]).lstrip("0") 
        if len(ans):
            return ans
        else :
            return "0"
         

num = "1234567890"
k = 9
print(removeKdigits(num,k))


