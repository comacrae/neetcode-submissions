# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def mergeSortRecursion(pairs:List[pair],s:int, e:int):

            def merge(pairs: List[pairs], s:int, m:int, e:int):
                L:List[Pair] = pairs[s:m+1]
                R:List[Pair] = pairs[m+1:e+1]
                i:int = 0
                j:int = 0
                k:int = s
                while i < len(L) and j < len(R):
                    if L[i].key <= R[j].key:
                        pairs[k] = L[i]
                        i+=1
                    else:
                        pairs[k] = R[j]
                        j+=1
                    k+=1
                while i < len(L):
                    pairs[k] = L[i]
                    i +=1
                    k +=1
                while j < len(R):
                    pairs[k] = R[j]
                    j +=1
                    k +=1
                return pairs
            
            # edge case: if len(arr) <= 1, it's already sorted
            if (e - s) + 1 <= 1:
                return pairs
            
            m:int = (e + s) // 2

            mergeSortRecursion(pairs, s, m)
            mergeSortRecursion(pairs,m+1, e)

            merge(pairs, s, m, e)
            return pairs
        
        return mergeSortRecursion(pairs, 0, len(pairs) - 1)

        
        


