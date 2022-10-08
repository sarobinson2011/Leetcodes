""" leetcode_58 modified to return the length of the longest word """


class Solution:

    def plusOne(self, digits: [int]) -> [int]:

        # temp = digits[::-1]
        # print(temp[0])

        if digits[::-1].count(9) == len(digits):
            digits[::-1].append(0)
            # print(temp)

        for i in range(len(digits[::-1])):
            if digits[::-1][i] == 9:
                digits[::-1][i] = 0
            else:
                digits[::-1][i] = digits[::-1][i] + 1
                break

        print(temp[::-1])


sol = Solution()
sol.plusOne([4, 3, 2, 1])  # return [4,3,2,2]
sol.plusOne([9])        # return [1,0]
sol.plusOne([9, 9])      # return [1,0,0]

