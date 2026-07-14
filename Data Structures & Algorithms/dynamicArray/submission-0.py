class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity:int = capacity
        self.nums: list[int] = []
        self.len = 0


    def get(self, i: int) -> int:
        return self.nums[i]


    def set(self, i: int, n: int) -> None:
        self.nums[i] = n


    def pushback(self, n: int) -> None:

        self.nums.append(n)
        self.len += 1

        # if over capacity, double capacity
        if self.capacity < self.len:
            self.resize()

    def popback(self) -> int:

        return_val:int = self.nums[self.len - 1]
        self.len -= 1
        return return_val
 

    def resize(self) -> None:
        self.capacity *=2


    def getSize(self) -> int:
        return self.len
        
    
    def getCapacity(self) -> int:
        return self.capacity
