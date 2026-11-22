# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxRecursive(self, root:Optional[TreeNode], currMax:int) -> int:
        if not root:
            return currMax
        return max(self.maxRecursive(root.left, 1 + currMax), self.maxRecursive(root.right, 1 + currMax))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is null, return the value passed in 
        return self.maxRecursive(root,0)
        