
""" SOLVED """

class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in s[::-1]:
            if i != " ":
                count += 1
            elif count > 0:
                return count
        return count


sol = Solution()
sol.lengthOfLastWord("a")
sol.lengthOfLastWord(" a")
sol.lengthOfLastWord("men__ 123  ")

