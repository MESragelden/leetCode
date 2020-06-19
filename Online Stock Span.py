class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        if (len(self.stack) == 0):
            self.stack.append([price,1])
            return 1 
        elif self.stack[-1][0]>price:
            self.stack.append([price,1])
            return 1
        else :
            result = 1
            while(len(self.stack )>0):
                if (self.stack[-1][0]<=price):
                    print(price , " ",result)
                    result += self.stack.pop()[1]
                else :
                    break
            self.stack.append([price,result])
            return result
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)