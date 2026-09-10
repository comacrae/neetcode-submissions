class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = target - nums[i]
        # diff : val
        # if diff in map, return i
        if len(nums) == 2:
            return [0,1]
        hashmap: dict[int,int] = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[diff],i]
        return

        