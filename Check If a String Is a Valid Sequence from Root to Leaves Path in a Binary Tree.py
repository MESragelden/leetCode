# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root, arr):
        length = len(arr)
        i = 0
        return self.path(root,arr,length,i)
    def path (self,root,arr,length,i):
        if root is None :
            return length==0 
        if (i==length-1) and (root.left == None and root.right == None) and (root.val == arr[i]):#leaf node
            return True
        if (i < length)and (root.val == arr[i]):
            return self.path(root.left,arr,length,i+1) or self.path(root.right,arr,length,i+1)

rl1 = TreeNode(0)
r = TreeNode(0,rl1)
llr = TreeNode(1)
ll = TreeNode(0,None,llr)
lrl = TreeNode(0)
lrr = TreeNode(0)
lr = TreeNode(1,lrl,lrr)
l = TreeNode(1,ll,lr)
root = TreeNode (0,l,r)
#[0,1,0,0,1,0,null,null,1,0,0], 
arr = [0,1,0,1]
s = Solution()
print(s.isValidSequence(root,arr))