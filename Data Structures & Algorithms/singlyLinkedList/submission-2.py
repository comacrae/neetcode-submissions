class LinkedList:
    class Node:
        def __init__(self, val:int = None, next: Node = None ):
            self.value: int = val
            self.next: Node | None = next
    
    def __init__(self):
        self.head: Node = self.Node() # dummy node
    
    def get(self, index: int) -> int:
        ptr: Node = self.head.next
        idx: int = 0

        while idx < index and ptr:
            ptr = ptr.next
            idx = idx + 1

        if ptr:
            return ptr.value
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        tmp: Node = self.head.next
        self.head.next = self.Node(val,tmp)
        return

        

    def insertTail(self, val: int) -> None:
        curr: Node = self.head
        while curr.next:
            curr = curr.next
        curr.next = self.Node(val, None)
        return
        

    def remove(self, index: int) -> bool:
        curr: Node = self.head.next
        prev: Node = self.head
        idx: int = 0
        while curr and idx < (index):
            curr = curr.next
            if curr:
                prev = prev.next
            idx = idx + 1

        if not curr:
            return False
        prev.next = curr.next
        
        return True

            
        
        

    def getValues(self) -> List[int]:
        output: List[int] = []
        curr: Node = self.head.next
        
        while curr:
            output.append(curr.value)
            curr = curr.next
        return output
        
