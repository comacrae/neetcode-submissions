class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr, m_ptr, r_ptr = 0 , 0, len(nums) - 1

        while(l_ptr <= r_ptr):
            m_ptr = (l_ptr + r_ptr) // 2 # int division
            
            if(target < nums[m_ptr]):
                r_ptr = m_ptr - 1
            elif (target > nums[m_ptr]):
                l_ptr = m_ptr + 1
            else:
                return m_ptr
        
        # if we reached this point, return -1
        return -1