import math 
s = set()
def sq(num):
    sum = 0 
    while num >0:
        r = num%10
        sum += r*r
        num = num //10
    return sum

def isHappy(n):
    sum_of_digits = sq(n)
    #print(sum_of_digits)
    while sum_of_digits not in s :
        if (sum_of_digits == 1):
            return True
    
        else :
            s.add(sum_of_digits)
        sum_of_digits = sq(sum_of_digits)
    return False
print(isHappy(28))


'''
s = set()
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sq(num):
            sum = 0 
            while num >0:
                r = num%10
                sum += r*r
                num = num //10
            return sum
        sum_of_digits = sq(n)
        while sum_of_digits not in s :
            if (sum_of_digits == 1):
                return True
            else :
                s.add(sum_of_digits)
            sum_of_digits = sq(sum_of_digits)
        return False
        

'''