# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left subtree, parent, right subtree
        # preorder: parent, left subtree, right subtree
        # postorder: left subtree, right subtree, parent
        if not root:
            return []
        arr = []
        arr += self.inorderTraversal(root.left)
        arr.append(root.val)
        arr += self.inorderTraversal(root.right)
        return arr
        
            
        