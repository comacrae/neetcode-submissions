# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root:Optional[TreeNode], val:int) -> TreeNode:
            #case 1: root is null
            newNode = TreeNode(val=val)
            if not root:
                return newNode
            
            if val < root.val:
                if not root.left:
                    root.left = newNode
                else:
                    root.left = insert(root.left, val)
            else:
                if not root.right:
                    root.right = newNode
                else:
                    root.right = insert(root.right, val)
            return root
        return insert(root, val)

            
        