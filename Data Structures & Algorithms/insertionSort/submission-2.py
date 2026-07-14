# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        steps: List[List[Pairs]] = [pairs.copy()]
        i: int = 1
        while i < len(pairs):
            j = i
            comp_pair = pairs[i]
            while j > 0 and pairs[j - 1].key > comp_pair.key:
                pairs[j] = pairs[j - 1]
                j = j - 1
            pairs[j] = comp_pair
            i = i + 1
            steps = steps + [pairs.copy()]
        return steps

