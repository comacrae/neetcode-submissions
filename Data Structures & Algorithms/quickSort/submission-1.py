# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def qSort(arr:List[Pair], s:int, e:int):
            if (e - s) + 1 <=1:
                return arr
            
            pivot:Pair = arr[e]
            left = s

            for i in range(s,e):
                if pairs[i].key < pivot.key:
                    tmp:Pair = pairs[i]
                    pairs[i] = pairs[left]
                    pairs[left] = tmp
                    left+=1
            tmp:Pair = pairs[left]
            pairs[left] = pivot
            pairs[e] = tmp
            
            qSort(arr, s, left-1)
            qSort(arr,left+1, e)

            return
        
        qSort(pairs,0, len(pairs) - 1)
        return pairs
        