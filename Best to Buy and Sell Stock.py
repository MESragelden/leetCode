def MaxProfit(L):
    size = len(L)
    result = 0
    new =[]
    for i in range(1,size):
            profit = L[i]-L[i-1]
            new.append(profit)
            if(profit > 0):
                result += profit
    return result




L = [7,1,5,3,6,4]
M = [1,2,3,4,5]
N = [7,6,4,3,1]
print(MaxProfit(N))