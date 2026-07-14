class Deque:
    
    def __init__(self):
        self.dq:list = []

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def append(self, value: int) -> None:
        self.dq.append(value)
        

    def appendleft(self, value: int) -> None:
        copy = [value]
        for val in self.dq:
            copy.append(val)
        self.dq = copy
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popped: int = self.dq[-1]
        self.dq = self.dq[:-1]
        return popped
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popped: int = self.dq[0]
        self.dq = self.dq[1:]
        return popped
        
