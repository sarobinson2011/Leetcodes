class Solution:
    def fibonacci(self, limit: int):
        out = [0, 1]
        for i in range(limit):
            temp = out[i] - out[i-1]
            out.append(temp)
            print('out =', out)


sol = Solution()
sol.fibonacci(5)

""" recursively calculate Fibonacci numbers (to the limit) """
