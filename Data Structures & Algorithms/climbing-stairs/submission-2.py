class Solution:
    def climbStairs(self, n: int) -> int:
        solutions : dict[int,int] = {}
        def func(n:int):
            if n <= 2:
                return n
            elif n in solutions.keys():
                return solutions[n]
            else:
                solution = func(n - 2) + func(n-1)
                solutions[n] = solution
                return solution
        return func(n)
        