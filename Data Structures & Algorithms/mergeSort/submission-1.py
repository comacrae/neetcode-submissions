# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, start:int, middle:int, end:int, pairs:List[Pair]):
        #make copies of the arrays
        left: List[Pair] = pairs[start:middle + 1]
        right: List[Pair] = pairs[middle + 1: end + 1]

        #go through each copy and compare elements, merging them in depending on value
        i: int = 0 # for tracking currently compared value in left pairs copy
        j: int = 0 # for tracking currently compared value in right pairs copy
        k: int = start # for tracking currently inserted value in pairs list

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
            else:
                pairs[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            pairs[k] = left[i]
            k +=1
            i +=1
        while j < len(right):
            pairs[k] = right[j]
            k += 1
            j  += 1
        
        return 
    def mSort(self,start:int, end:int, pairs:List[Pair]):
        # base-case: Only one element in the array 
        if (end-start) + 1 <= 1:
            return pairs
        # get middle idx of array
        middle = start + ((end-start) // 2)

        #recursively run mergesort on left side of array
        self.mSort(start, middle, pairs)

        #recursively run mergesort on right side of array
        self.mSort(middle+1, end, pairs)

        #merge the two together
        self.merge(start,middle, end, pairs)

        return pairs
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mSort(0, len(pairs) - 1, pairs)
