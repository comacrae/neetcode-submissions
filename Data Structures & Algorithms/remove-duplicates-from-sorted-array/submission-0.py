class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l: int = 0
        r: int = 0
        n: int = len(nums)

        while r < n: # while right pointer is still in bounds
            nums[l] = nums[r] #swap l and r (store current val)
            # now we find next non-unique value
            while r < n and nums[l] == nums[r]:
                r += 1
            # at this point we found the next val to store
            #shift l up so we dont overwrite it
            l += 1
        return l
            
        
            
            

        