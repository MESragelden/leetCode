class doubleLinkedList:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = doubleLinkedList(-1,-1)
        self.tail = self.head
        self.hash = {}
        self.capacity = capacity  
        self.length  = 0
    def get(self, key: int) -> int:
        if  key not in self.hash:
            return -1
        node = self.hash[key]
        if(node.next is not None):
            node.next.prev = node.prev
            node.prev.next = node.next
            self.tail.next = node
            self.tail = node
            node.prev = self.tail 
            node.next = None
        return node.value        
    def put(self, key: int, value: int) -> None:
        if key not in self.hash :
            node = doubleLinkedList(key,value)
            self.hash[key] = node 
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            self.length +=1
            if self.length >self.capacity :
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -=1
        else :
            node = self.hash[key]
            if(node.next is not None):
                node.next.prev = node.prev
                node.prev.next = node.next
                self.tail.next = node
                self.tail = node
                node.prev = self.tail 
                node.next = None
            node.value = value


'''
cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
print(cache.get(2))
cache.put(3,3)
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
'''
cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
'''["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
'''
["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
[[10],
[10,13],
[3,17],
[6,11],
[10,5],
[9,10],
[13],[2,19],
[2],[3],[5,25],
[8],[9,22],
[5,5],
[1,30],
[11],[9,12]
,[7],[5],[8],[9],[4,30]
,[9,3]
,[9],[10],[10],[6,14],
[3,1],[3],[10,11],
[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]