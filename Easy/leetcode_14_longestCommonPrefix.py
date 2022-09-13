class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Find longest common prefix
        result = ""
        if strs is None or len(strs) == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        minimum_length = len(strs[0])
        for i in range(1, len(strs)):
            minimum_length = min(minimum_length, len(strs[i]))
        for i in range(0, minimum_length):
            current = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return result
            result += current
        return result


sol = Solution()
sol.longestCommonPrefix(["flower", "flow", "flight"])
