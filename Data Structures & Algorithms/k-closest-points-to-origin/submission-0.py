class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def eDist(point:List[int]):
            xi:int = point[0]
            yi:int = point[1]
            return ((xi**2) + (yi**2)) ** 0.5

        def quickSort(points:List[List[int]], s:int, e:int):
            if e - s + 1 <= 1: # if len(arr) <=1 (basecase)
                return

            pivot = points[e]
            left = s

            for i in range(s, e + 1):
                if eDist(points[i]) < eDist(pivot):
                    tmp:List[int] = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1
            
            tmp:List[int] = points[left]
            points[left] = pivot
            points[e] = tmp
            
            quickSort(points,s,left - 1)
            quickSort(points,left+1, e)
            return
        quickSort(points, 0, len(points)-1)
        return points[:k]
            
