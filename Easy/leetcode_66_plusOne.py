"""             SOLVED!

    run time: 32 ms (beats 95.82%)
    memory: 13.8 MB (beats 96.26%)

"""

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        temp = digits[::-1]
        if temp.count(9) == len(digits):
            temp.append(0)
        for i in range(len(temp)):
            if temp[i] == 9:
                temp[i] = 0
            else:
                temp[i] = temp[i] + 1
                break
        return temp[::-1]