# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMinNode(root:TreeNode) -> TreeNode:
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def removeNode(root:Optional[TreeNode], key:int) -> Optional[TreeNode]:
            if not root:
                return None
            
            if key < root.val:
                root.left = removeNode(root.left, key)
            elif key > root.val:
                root.right = removeNode(root.right, key)
            else:
                if root.left and root.right:
                    root.val = getMinNode(root.right).val
                    root.right = removeNode(root.right, root.val)
                else:
                    if not root.left:
                        root = root.right
                    else:
                        root = root.left
            return root
        
        return removeNode(root, key)