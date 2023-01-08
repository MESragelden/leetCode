import math
from collections import Counter

def maxPoints(points):
    if len(points) == 1:
        return 1 
    maxi = 0 
    dict = {}
    for i in range(len(points)-1):
        for j in range (i+1,len(points)):
            s = slope(points[i],points[j])
            if s in dict:
                dict[s].append(points[i])
            else : 
                dict[s] = [points[i]]
    
    for v in dict.values():
        count = {}
        for ele in v:
            p = str(ele[0]) + ',' + str(ele[1])
            if p not in count:
                count[p] = 1
            else :
                count[p]+= 1
        if max(count.values()) > maxi:
            maxi = max(count.values())
        
        

    return maxi+1
    # values = max(dict.values())
        
    # i = 1
    # while values != 0:
    #     values -= i
    #     i += 1
    # return i

def slope(a,b):
    if (b[0] - a[0])!= 0:
        s = (b[1] - a[1])/(b[0] - a[0])
    else :
        return "Not a number"
    return s 
        

points = [[1,1],[2,2],[3,3]]
points1 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points2 = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
points3 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(maxPoints(points))
print(maxPoints(points1))
print(maxPoints(points2))
print(maxPoints(points3))