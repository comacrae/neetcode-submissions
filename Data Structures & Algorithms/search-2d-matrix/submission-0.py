class Solution:
    def searchRow(self, row: List[int], target:int) -> bool:
        l_ptr, m_ptr, r_ptr = 0,0,len(row)

        while l_ptr <= r_ptr:
            m_ptr = (l_ptr + r_ptr) //2
            val = row[m_ptr]

            if( target < val):
                r_ptr = m_ptr - 1
            elif (target > val): 
                l_ptr = m_ptr + 1
            else:
                return True
        
        return False



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_bottom, row_top, row_mid, = len(matrix) - 1,0,0


        while(row_top <= row_bottom):
            row_mid = (row_top + row_bottom) // 2

            if target < matrix[row_mid][0]:
                row_bottom = row_mid - 1
            elif target > matrix[row_mid][-1]:
                row_top = row_mid + 1
            else:
                return self.searchRow(matrix[row_mid], target)
        return False



        