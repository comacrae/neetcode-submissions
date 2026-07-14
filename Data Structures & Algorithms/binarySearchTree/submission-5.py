class TreeNode:
    def __init__(self, 
    key:int = 0, 
    val:int = 0, 
    left = None, 
    right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:

    def __init__(self):
        self.root = None

    def get_min_or_max_node(self, get_min=False):
        curr = self.root
        if not curr:
            return None
        if get_min:
            while curr.left:
                curr = curr.left
        else:
            while curr.right:
                curr = curr.right
        return curr
    def insert(self, key: int, val: int) -> None:

        def insert_dfs(root, key, val):
            if not root:
                return TreeNode(key=key,val=val)
            
            if key < root.key:
                root.left = insert_dfs(root.left,key,val)
            elif key > root.key:
                root.right = insert_dfs(root.right, key,val)
            else:
                root.val = val
            return root

        self.root = insert_dfs(self.root,key,val)
        return



    def get(self, key: int) -> int:
        def search_dfs(root, key):
            if not root:
                return None
            if key < root.key:
                return search_dfs(root.left,key)
            elif key > root.key:
                return search_dfs(root.right,key)
            else:
                return root.val
        output = search_dfs(self.root,key)
        return -1 if output is None else output

    def getMin(self) -> int:
        output_node = self.get_min_or_max_node(get_min = True)
        return output_node.val if output_node else -1


    def getMax(self) -> int:
        output_node = self.get_min_or_max_node(get_min = False)
        return output_node.val if output_node else -1



    def remove(self, key: int) -> None:
        def remove_dfs(root, key):
            if not root:
                return None
            if key < root.key:
                root.left = remove_dfs(root.left, key)
            elif key > root.key:
                root.right = remove_dfs(root.right,key)
            else:
                if not root.left and not root.right:
                    root = None
                elif not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    min_node = root.right
                    while min_node and min_node.left:
                        min_node = min_node.left
                    root.key = min_node.key
                    root.val = min_node.val
                    root.right = remove_dfs(root.right,root.key)
            return root
        self.root = remove_dfs(self.root,key)
        return


    def getInorderKeys(self) -> List[int]:
        def list_bfs(root,output):
            if not root:
                return output
            output = list_bfs(root.left, output)
            output.append(root.key)
            output = list_bfs(root.right, output)
            return output
        return list_bfs(self.root, [])



