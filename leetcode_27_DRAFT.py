""" working solution for leetcode_27 removeElement """


class Solution:

    def removeElement(self, nums: [int], val: int) -> int:
        k = 1
        for i in range(len(nums)):
            if nums[-i] == val:
                nums.pop(-i)
                nums.append(0)
            else:
                k += 1
        print("mid solution = ", nums)
        print("K = ", k)


sol = Solution()
sol.removeElement([1, 1, 1, 4, 1, 0], 1)

# sol.removeElement([3, 2, 2, 3], 3)
# sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)


