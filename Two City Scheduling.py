def twoCitySchedCost(costs):
    (costs.sort(key=lambda x: (x[0]-x[1])))
    print(costs)
    result = 0
    for i in range (len(costs)):
        if i < (len(costs)/2):
            result += costs[i][0]
        else : 
            result += costs[i][1]
    return result


l = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(l))
        