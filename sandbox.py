class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word = min(strs, key=len)
        strs.remove(shortest_word)
        result = ""
        # loop  (i)  through the list of strings - looking for the shortest string
        for i in range(len(strs)):
            # for each string - loop  (j)  through the individual letters in the shortest string
            for j in range(len(shortest_word)):
                # check if the letter in the shortest string == the letter in current string
                if current_word[j] == shortest_word[j]:
                    # add the letter to the result string
                    result += shortest_word[j]


sol = Solution()
sol.longestCommonPrefix(["flower", "flow", "flight"])








