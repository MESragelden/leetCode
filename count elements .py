def countElements(arr):
    d = dict()
    for ele in arr:
        exist = d.get(ele,0)
        if exist:
            d[ele]+=1
        else:
            d[ele]=1
    exist = 0
    counter =0
    for ele in d.keys():
        exist = d.get(ele+1,0)
        if exist:
            counter += d[ele]
    return counter







L = [1,2,3]#2
M = [1,1,3,3,5,5,7,7] #0
N = [1,3,2,3,5,0] #3
O = [1,1,2,2] #2
Q = [1,1,2]
print(countElements(M))