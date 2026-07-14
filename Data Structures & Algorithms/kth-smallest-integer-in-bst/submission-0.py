# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getTreeSortedInorder(self, root:Optional[TreeNode], output: list[int]) -> list[int]:
        if root is not None:
            output = self.getTreeSortedInorder(root.left, output)
            output.append(root.val)
            output = self.getTreeSortedInorder(root.right,output)
        return output
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        output = self.getTreeSortedInorder(root, output)
        return output[k-1]
        