""" leetcode_58 modified to return the length of the longest word """


class Solution:

    def lengthOfLongestWord(self, s: str) -> int:
        count = 0
        store = []
        # for c in s[::-1]:
        for c in s[::-1]:

            if c != "-":
                count += 1
            elif count > 0:
                store.append(count)
                count = 0

        store.append(count)
        print(max(store))
        return max(store)


sol = Solution()
sol.lengthOfLongestWord("a")               # return 1
sol.lengthOfLongestWord("-a")              # return 1
sol.lengthOfLongestWord("meme--11111123--")     # return 4

