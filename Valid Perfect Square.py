def isPerfectSquare(num):
        import math
        r = math.sqrt(num)
        t = str(r).split('.')
        return int(t[1]) == 0
        



print(isPerfectSquare(14))