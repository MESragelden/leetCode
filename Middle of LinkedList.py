# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tr = head
        count = 0
        while tr is not None:
            tr = tr.next
            count +=1
        return count
l = [1,2,3,4,5]
m = ListNode(l)
print(m.middleNode(m))
        