# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None :
            return head
        odd = head        
        even = head.next
        st_even = even 
        while odd.next:
            if odd.next.next:   
                odd.next = odd.next.next
                #print(odd.next)
                odd = odd.next
                if(odd.next):
                    even.next = odd.next
                    even = even.next
                else :
                    even.next = None
            else :
                #print (head)
                odd.next = st_even
                print (head)
                return head

        odd.next = st_even
        print (head)
        return head
     