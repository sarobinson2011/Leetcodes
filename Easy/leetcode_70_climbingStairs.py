""" working solution to leetcode_70_climbingStairs  - SOLVED (beats: runtime - 70.7% / memory - 57.32%"""


class Solution:

    def climbStairs(self, n: int) -> int:
        res = [1, 1]
        for i in range(1, n):
            temp = res[-1] + res[-2]
            res.append(temp)
        print(res[-1])
        return res[-1]

            # with open('output.txt', 'w') as f:
            #     print(f'\nFibonacci numbers: {res}', file=f)


sol = Solution()
sol.climbStairs(1)
sol.climbStairs(2)
sol.climbStairs(3)
sol.climbStairs(4)
sol.climbStairs(5)
sol.climbStairs(6)
sol.climbStairs(7)
# Fibonacci numbers:  1, 1, 2, 3, 5, 8, 13, 21
