class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map: dict[int,int] = {}
        result = []
        for num in nums:
            if num in freq_map:
                freq_map[num]+= 1
            else:
                freq_map[num] = 1
        freq_list: List[List[int]] = [[] for i in range(len(nums) + 1)  ] 
        for num, freq in freq_map.items():
            freq_list[freq].append(num)
        idx = len(freq_list) - 1
        while idx >= 0 and len(result) < k:
            if len(freq_list[idx]) != 0:
                result.append(freq_list[idx].pop())
            else:
                idx -=1
        return result
