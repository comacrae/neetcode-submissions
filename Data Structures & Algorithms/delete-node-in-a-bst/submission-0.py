# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minNode(root:TreeNode) -> TreeNode:
            curr = root
            while curr.left:
                curr = curr.left
            return curr

        def delNode(root:Optional[TreeNode], val:int) -> Optional[TreeNode]:
            if not root: # if root dne
                return None

            # find node to delete

            if val > root.val:
                root.right = delNode(root.right, val)
            elif val < root.val:
                root.left = delNode(root.left, val)
            else: # we found the node to delete
                # 3 cases - no children, 1 child, 2 children
                if not root.left and not root.right:
                    root = None
                elif root.left and not root.right: 
                    root = root.left
                elif root.right and not root.left:
                    root = root.right
                elif root.right and root.left:
                    minChild = minNode(root.right)
                    root.val = minChild.val
                    root.right = delNode(root.right, root.val)
            return root
        return delNode(root, key)



        