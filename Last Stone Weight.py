import heapq
def lastStoneWeight(List):
    
    
    while (len(List)>1):
        heapq._heapify_max(List)
        a = heapq.heappop(List)
        heapq._heapify_max(List)
        b = heapq.heappop(List)
        if (a != b):
            heapq.heappush(List,a-b)
   
    return (List[0])
    

l = [2,7,4,1,8,1]
print(lastStoneWeight(l))