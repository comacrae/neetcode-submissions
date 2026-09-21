class Node:
    def __init__(self,key=0, val=0, prev=None, next=None):
        self.key:int = key
        self.val:int = val
        self.prev: Node = prev
        self.next: Node = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache: dict[int,Node] = {}
        self.list_head: Node = Node()
        self.list_tail: Node = Node()
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        self.capacity = capacity
    """
        1. LL is empty; put on top
        2. LL has value already: get and move to top
        3. LL doesnt have value and isnt empty;
        """
    def _remove(self,node:Node):
        #remove node from current position
            node.next.prev = node.prev
            node.prev.next = node.next
            return

    def _put_in_front(self,node:Node):
        # move node to top of list
        node.next = self.list_head.next
        node.prev = self.list_head

        self.list_head.next.prev = node
        self.list_head.next = node
        return

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node:Node = self.cache[key]
            self._remove(node)
            self._put_in_front(node)
            #return the node's value
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #remove if capacity is exceeded
        

        if key in self.cache.keys():
            #remove node from current position
            node: Node = self.cache[key]
            self._remove(node)
            # move node to top of list
            self._put_in_front(node)
            #update the existing value
            node.val = value
        else:
            if len(self.cache.keys()) == self.capacity:
                removed: Node = self.list_tail.prev
                self._remove(removed)
                del self.cache[removed.key]
            node:Node = Node(key,value)
            self._put_in_front(node)
            self.cache[key] = node
        return 

        



        
