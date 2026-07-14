class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low: int = 1
        high: int = max(piles) # highest viable would be eating_rate = max
        best_rate: int = high

        while low<= high:
            mid = (low + high) // 2
            time_to_eat:int = 0
            for pile in piles:
                time_to_eat += math.ceil(float(pile)/mid)
            if time_to_eat <= h:
                best_rate = mid
                high = mid - 1
            else:
                low = mid + 1
        return best_rate
