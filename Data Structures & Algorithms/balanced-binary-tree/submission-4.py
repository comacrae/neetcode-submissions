# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root:Optional[TreeNode], height:int) -> (bool, int):
            if not root:
                return True, height
            l_balanced, l_height = dfs(root.left, height + 1)
            if not l_balanced:
                return False, 0
            r_balanced, r_height = dfs(root.right, height + 1)
            if not r_balanced:
                return False, 0
            is_balanced = (abs(l_height - r_height) <= 1) and l_balanced and r_balanced

            return is_balanced, max(l_height, r_height)
        return dfs(root,0)[0]
        