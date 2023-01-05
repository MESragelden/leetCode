
def findMinArrowShots(points):
    if len(points)== 0:
        return 0 
    count = 1 
    points.sort(key=lambda x: x[0])
    last = points[0][1]
    i = 1
    while i < len(points):
        if points[i][0] <=  last:
            last = min(last, points[i][1])
            i += 1 
        else :
            count += 1 
            last = points[i][1]
            i +=1 
    return count






points = [[10,16],[2,8],[1,6],[7,12]]
points1 = [[1,2],[3,4],[5,6],[7,8]]
points2 = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))
print(findMinArrowShots(points1))

print(findMinArrowShots(points2))
points4 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(findMinArrowShots(points4))
        