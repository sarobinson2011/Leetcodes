""" leetcode 35 - Search Insert solution  """

""" Right first time!!!!! """


class Solution:

    def searchInsert(self, nums: [int], target: int) -> int:

        if nums[-1] < target:
            nums.append(target)
            # print(len(nums)-1)
            return len(nums)-1

        for i in range(len(nums)):
            if nums[i] == target:
                # print(i)
                return i
            elif nums[i] > target:
                nums.insert(i, target)
                # print(i)
                return i


sol = Solution()
sol.searchInsert([1, 3, 5, 6], 1)       # returns 0
# sol.searchInsert([1, 3, 5, 6], 2)     # returns 1
# sol.searchInsert([1, 3, 5, 6], 4)     # returns 2
# sol.searchInsert([1, 2, 3, 6], 7)     # returns 4



