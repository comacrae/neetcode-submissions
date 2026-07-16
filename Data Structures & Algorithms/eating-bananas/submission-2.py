class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatPilesWithRateK(piles, k) -> bool:
            def ceilDivide(m,n):
                if m % n == 0:
                    return m // n
                else:
                    return (m // n) + 1

            totalHours:int = 0

            for pile in piles:
                totalHours += ceilDivide(pile,k)
            
            return totalHours <= h
        
        L, R = 1, max(piles)
        lowestK = max(piles)
        while L <= R:
            mid = (L + R) // 2
            if canEatPilesWithRateK(piles,mid):
                lowestK = mid
                R = mid - 1
            else:
                L = mid + 1
        return lowestK


            