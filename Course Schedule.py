def canFinish(numCourses, prerequisites):
    import collections
    indegree= collections.defaultdict(set)
    outdegree= collections.defaultdict(set)
    for x,y in prerequisites :
        indegree[x].add(y)
        outdegree[y].add(x)
    removed_conn = 0
    indegree_zeros = [] 
    for i in range (numCourses):
        if not indegree[i]:
            indegree_zeros.append(i)
            removed_conn +=1
    while indegree_zeros:
        node = indegree_zeros.pop()
        for x in outdegree[node]:
            indegree[x].remove(node)
            if not indegree[x]:
                indegree_zeros.append(x)
                removed_conn +=1
    return removed_conn == numCourses

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses,prerequisites))
        