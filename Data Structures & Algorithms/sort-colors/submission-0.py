class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3 # for vals 0, 1, 2 
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        i = 0
        for j in range(len(counts)):
            for k in range(counts[j]):
                nums[i] = j
                i += 1
        return