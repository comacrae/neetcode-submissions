# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getBSTHeight(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(getBSTHeight(root.left), getBSTHeight(root.right))
        
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if abs(getBSTHeight(root.left) - getBSTHeight(root.right)) > 1:
            return False
        if not self.isBalanced(root.right):
            return False
        
        return True

