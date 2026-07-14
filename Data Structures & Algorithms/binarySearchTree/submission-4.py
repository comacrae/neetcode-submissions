class TreeMap:
    class TreeNode:
        def __init__(
            self, 
            val:int = 0, 
            key:int = 0,
            left= None, 
            right = None
            ):
            self.val:int = val
            self.key:int = key
            self.left: Optional[TreeNode] = left
            self.right: Optional[TreeNode] = right
            return
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
        return
    
    def inorderTraversal(self,root:Optional[TreeNode], output:List[int]):
        if not root:
            return output
        output = self.inorderTraversal(root.left, output)
        output.append(root.key)
        output = self.inorderTraversal(root.right, output)
        return output

    def getMinNode(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        curr: TreeNode = root
        if not curr:
            return None
        while curr.left:
            curr = curr.left
        return curr

    def removeDFS(self, root:Optional[TreeNode], key:int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.key:
            root.left = self.removeDFS(root.left, key)
        elif key > root.key:
            root.right = self.removeDFS(root.right,key)
        else: #  key == root.key
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else: # 2 children
                min_node: TreeNode = self.getMinNode(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.removeDFS(root.right, min_node.key)
        return root
    def searchDFS(self, root:Optional[TreeNode], key:int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.searchDFS(root.left, key)
        else:
            return self.searchDFS(root.right,key)
        
    def insertDFS(self, root: Optional[TreeNode], key: int, val:int) -> TreeNode:
        #need to insert as leaft that satisfies condition of BSTs:
        # all values in left subtree < root value
        # all values in right subtree > root value

        if not root: # if at leaf (or empty tree) create and return node
            return self.TreeNode(key=key, val=val)
        
        if key == root.key:
            root.val = val
        elif key < root.key: # assign as leaf in left subtree
            root.left = self.insertDFS(root.left, key, val)
        else:
            root.right = self.insertDFS(root.right, key, val)
        return root

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertDFS(self.root, key, val)

    def get(self, key: int) -> int:
        result_node: Optional[TreeNode] = self.searchDFS(self.root,key)
        if not result_node:
            return -1
        return result_node.val

    def getMin(self) -> int:
        min_node: Optional[TreeNode] = self.getMinNode(self.root)
        return min_node.val if min_node else -1

    def getMax(self) -> int:
        curr: TreeNode = self.root
        if not curr:
            return -1
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeDFS(self.root, key)
        return

    def getInorderKeys(self) -> List[int]:
        output: List[int] = []
        return self.inorderTraversal(self.root, output)


