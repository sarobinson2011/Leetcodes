class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word = min(strs, key=len)
        results = []
        result = ""
        # loop  (i)  through the list of strings - looking for the shortest string
        for i in range(len(strs)):
            # check that result doesn't contain the shortest string
            if result != shortest_word:
                # disregard comparison of the shortest word against itself
                if strs[i] != shortest_word:
                    current_word = strs[i]
                    # loop  (j)  through the individual letters in the shortest string
                    for j in range(len(shortest_word)):
                        # check if the letter in the shortest string == the letter in current string
                        if current_word[j] == shortest_word[j]:
                            # add the letter to the result string
                            result += shortest_word[j]
                            # is this required ???  todo
                            results.append(result)
                else:
                    continue
            else:
                break
        # answer = min(results, key=len) # todo
        # answer = result
        print(result)
        return result


sol = Solution()
sol.longestCommonPrefix(["flower", "flow", "flight"])








