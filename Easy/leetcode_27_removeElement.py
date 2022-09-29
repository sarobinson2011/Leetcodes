""" leetcode_27 removeElement - working solution """

class Solution:
    def removeElement(self, nums: [int], val: [int]) -> int:
        k = 0
        length = len(nums)

        for i in range(length):
            temp = nums[i]
            if temp != val:
                nums[k] = nums[i]
                k += 1

        print("nums = ", nums)
        print("count =", k)
        return k


sol = Solution()
# sol.removeElement([1], 1)
# sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
sol.removeElement([3,2,2,3], 3)
# sol.removeElement([0, 0, 0, 0, 0, 0, 0], 4)
