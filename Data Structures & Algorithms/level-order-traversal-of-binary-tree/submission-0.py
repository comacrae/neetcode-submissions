# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output:List[List[int]] = []
        queue: collections.deque = deque()
        
        if root:
            queue.append(root)

        while len(queue) > 0:
            level: List[int] = []
            num_nodes: int = len(queue)
            for i in range(0, num_nodes): # for each level in tree
                #get node i from level
                node = queue.popleft()
                # add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # add node value to level's list
                level.append(node.val)
            # add level list to output list of lists
            output.append(level)
        return output
