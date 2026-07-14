class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []
        return
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)
        return
        

    def pop(self) -> None:
        top_val:int = self.top()
        if self.min_stack[-1] == top_val:
            self.min_stack = self.min_stack[:-1]
        self.stack = self.stack[:-1]

        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
