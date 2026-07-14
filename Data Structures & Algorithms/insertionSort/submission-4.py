# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        """
        Iterative Insertion sort steps:
        1. Start with two pointers; one at idx 1, other at 0
        2. for each iteration, the following pointer (j) does this check:
        a. is the value in front of me (i to start) smaller than me?
        YES:
        i. Swap the value in front of me with myself. This makes the value thats smaller go back
        ii. Keep doing this until this value no longer is smaller than values behind it OR hit idx 0
        NO:
        go to next iteration
        """
        output: List[List[Pair]] = [pairs[:]] if len(pairs) else []
        
        

        for i in range(1, len(pairs)):
            j: int = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                tmp:Pair = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j -= 1
            output.append(pairs[:])
        return output
        