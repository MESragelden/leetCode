# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) :
        def ORDER(preorder):          
            if preorder is None or len(preorder)==0:
                return 

            tn=TreeNode(preorder[0])
            if len(preorder)==1:
                return tn
            root = preorder[0]
            for i in range(1,len(preorder)):
                if preorder[i]>root:
                    break
            if i == (len(preorder)-1) and preorder[-1]<tn.val :
                left = preorder[1:]
                right = []
            else :
                left = preorder[1:i]
                right = preorder[i:]
            #printprint(left," ",root," ",right)
            if(len(left)>0):
                tn.left = ORDER(left)
            if len(right)>0:
                tn.right = ORDER(right)
            
            
            return tn
        
        if preorder is None or len(preorder)==0:
            return 
        return ORDER(preorder)

            
l = [8,5,1,7,10,12]
l3 = [4,2]
s = Solution()
print(s.bstFromPreorder(l3))