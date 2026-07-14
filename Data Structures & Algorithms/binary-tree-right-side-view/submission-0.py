# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output: List[int] = []
        queue: collections.deque = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            num_nodes: int = len(queue)
            for i in range(0, num_nodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == num_nodes - 1: # if right-most node in level
                    output.append(node.val)
        return output
                            