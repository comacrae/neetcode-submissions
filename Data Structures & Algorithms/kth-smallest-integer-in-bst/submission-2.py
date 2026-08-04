# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #if you traverse a binary tree in-order, you get the sorted values of the tree
        sorted_values: list[int] = []
        def inorder(root:Optional[TreeNode]) -> None:
            if not root:
                return
            inorder(root.left)
            sorted_values.append(root.val)
            inorder(root.right)
            return
        inorder(root)
        return sorted_values[k-1]

        