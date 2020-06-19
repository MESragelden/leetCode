# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self, root: TreeNode)->int:
        if root == None : 
            return 0
        else :
            return 1+max(self.height(root.right),self.height(root.left))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if (root == None):
            return 0
        h_Left = self.height(root.left)
        h_right = self.height(root.right)

        d_Left = self.diameterOfBinaryTree(root.left)
        d_right = self.diameterOfBinaryTree(root.right)
        return max(h_Left+h_right,max(d_Left,d_right))

t = TreeNode(8)
s = Solution()
print(s.height(t))