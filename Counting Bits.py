def countBits(num):
    def cal (de):
        bi = bin(de)
        sum = 0
        for i in bi :
            if i == '1':
                sum+=1
        return sum
    out = []
    for i in range (0,num+1):
        out.append(cal(i))
    return out
print(countBits(2))        