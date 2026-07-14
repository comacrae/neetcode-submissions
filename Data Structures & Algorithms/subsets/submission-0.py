class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output: List[List[int]] = []
        def treeMaze(nums: List[int], idx:int):
            #base case
            if idx >= len(nums):
                output.append(nums)
                return
            pop_list = [num for i,num in enumerate(nums) if i != idx ]
            treeMaze(pop_list, idx)
            idx +=1
            treeMaze(nums, idx)
            return
        treeMaze(nums,0)
        return output