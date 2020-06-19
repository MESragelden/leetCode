def reconstructQueue(people):
    class Foo(list):
        def __lt__(self, other):    
            return self[0] < other[0] or (self[0] == other[0] and self[1] > other[1])

    new_list = sorted(people, key=Foo)
    #print(sorted(people))
    #li = sorted(people, key = lambda x:(-x[1], x[0]))
    print(new_list)
    outputlist = [0 for i in range(len(people))] 
    indexes = [i for i in range(len(people))]
    print(indexes)
    for ele in new_list:
        index = indexes[ele[1]]
        outputlist[index] = ele
        indexes.remove(index)
    return outputlist



p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(reconstructQueue(p))

        