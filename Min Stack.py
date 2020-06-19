class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> None:
        if(len(self.l)>0):
            self.l.pop()

    def top(self) -> int:
        if (len(self.l)>0):
            return self.l[-1]

    def getMin(self) -> int:
        return min(self.l)



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
param_4 = obj.getMin()
print(param_4,obj.l)
obj.pop()
param_4 = obj.getMin()
print(param_4,obj.l)
obj.pop()
param_4 = obj.getMin()
print(param_4,obj.l)
obj.pop()
param_4 = obj.getMin()
print(param_4,obj.l)
'''
["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
[[],        [2],    [0],   [3],   [0],   [],      [],   [],[],[],[],[]]

'''