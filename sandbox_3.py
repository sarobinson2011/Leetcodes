""" leetcode 26 - remove duplicates from a sorted array """

class Solution:
    def remove_duplicates(self, nums: [int]) -> int:
        length = len(nums)-1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                nums.append(0)
            else:
                continue

        print("mid answer = ", nums)

        for i in nums[::-1]:
            if nums[i] == 0:
                length -= 1
            else:
                print("int answer is: ", length)
                return length


sol = Solution()
sol.remove_duplicates([0, 0, 1, 1, 2, 3, 3, 4, 4, 5])
# sol.remove_duplicates([1, 1, 2])

