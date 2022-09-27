""" leetcode 26 - remove duplicates from a sorted array - SOLVED"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[-i] > nums[-i-1]:
                count += 1
            else:
                nums.pop(-i)
                nums.append(0)
        return count


sol = Solution()
# sol.remove_duplicates([0, 1, 1, 1, 2, 2, 3, 4, 9])
# sol.remove_duplicates([0, 0, 0, 0, 1, 1, 3])
sol.remove_duplicates([0, 1, 1, 2])

