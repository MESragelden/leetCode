def kClosest(points, K):
    import math
    dic = dict()
    for point in points : 
        dist = math.sqrt(point[0]**2 + point[1]**2)
        dic[(point[0],point[1])] = dist
    dic  = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
    out = []
    i = 0 
    for ele in dic:
        if i<K:
            out.append(list(ele))
            i +=1
        else :
            break
    return out

points = [[1,3],[-2,2]]
K = 1
print(kClosest(points,K))