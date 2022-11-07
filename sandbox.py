class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        length = min(m, n)
        for i in range(length):
            if nums1[i] <= nums2[i]:
                nums1.insert(i+1, nums2[i])
                print(nums1)


sol = Solution()
sol.merge([1,1,3,0,0], 3, [2,4], 2)
# Output: [1,2,2,3,4]


# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
#
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

