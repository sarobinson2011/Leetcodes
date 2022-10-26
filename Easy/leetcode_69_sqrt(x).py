# Solution to leetcode #69 - sqrt(x) -- SOLVED

class Solution:
    def mySqrt(self, x: int) -> int:

        num = 1
        temp = []

        for i in range(100):
            num = (num + x / num) / 2
            temp.append(num)

            if i > 0:
                if round(temp[i], 3) == round(temp[i-1], 3):
                    out = temp[i]
                    print(int(out))
                    break


sol = Solution()
sol.mySqrt(13)