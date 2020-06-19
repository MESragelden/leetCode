class FirstUnique:

    def __init__(self, nums):
        self.listOFUnique =[]
        self.d = dict()
        for ele in nums:
            self.add(ele)

    def showFirstUnique(self) -> int:
        if (self.showFirstUnique)==0:
            return -1
        else :
            if(len(self.listOFUnique)>0):
                print(self.listOFUnique[0])
                return self.listOFUnique[0]
            else :
                print (-1)
                return -1

    def add(self, value: int) -> None:
        if value in self.d:
            if self.d[value]==1:
                self.d[value]+=1
                self.listOFUnique.remove(value)
        else :
            self.listOFUnique.append(value)
            self.d[value] = 1
        


# Your FirstUnique object will be instantiated and called as such:
#obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
firstUnique = FirstUnique([2,3,5])
firstUnique.showFirstUnique() # return 2
firstUnique.add(5);            # the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); # return 2
firstUnique.add(2);            # the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); # return 3
firstUnique.add(3);            # the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); # return -1