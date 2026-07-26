# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #height is the number of edges from the root node to the longest path to a leaf node 
        def getHeight(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)

            return 1 + max(leftHeight,rightHeight)
        
        if not root:
            return True
        
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        elif self.isBalanced(root.left) and self.isBalanced(root.right):
            return True   
        else:
            return False     
        
        
        