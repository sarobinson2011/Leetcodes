class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  temporary storage array
        temp = []

        # store the non-zeros in temp[]
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        # calculate the number of zeros required
        zeros = len(nums) - len(temp)

        # append the zeros to temp[]
        for i in range(zeros):
            temp.append(0)

        # copy the temp[] back to nums[]
        nums = temp

        print("nums =", nums)


sol = Solution()
# sol.moveZeroes([ 1, 5, 0, 0, 2 ])
# sol.moveZeroes([0])
sol.moveZeroes([ 0, 1, 0, 3, 12 ])
