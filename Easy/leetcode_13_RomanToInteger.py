class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dict_s = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if len(s) == 1:
                num = num + dict_s.get(s[i])
            else:
                if s[i] == "I":
                    if i < len(s)-1:
                        if s[i + 1] == "I":
                            num = num + dict_s.get(s[i])
                        else:
                            num = num - dict_s.get(s[i])
                    else:
                        num = num + dict_s.get(s[i])
                if s[i] == "V":
                    num = num + dict_s.get(s[i])
                elif s[i] == "X":
                    if i < len(s)-1:
                        if s[i + 1] == "L":
                            num = num - dict_s.get(s[i])
                        elif s[i + 1] == "C":
                            num = num - dict_s.get(s[i])
                        else:
                            num = num + dict_s.get(s[i])
                    else:
                        num = num + dict_s.get(s[i])
                elif s[i] == "L":
                    num = num + dict_s.get("L")
                elif s[i] == "C":
                    if i < len(s) - 1:
                        if s[i + 1] == "D":
                            num = num - dict_s.get(s[i])
                        elif s[i + 1] == "M":
                            num = num - dict_s.get(s[i])
                        else:
                            num = num + dict_s.get(s[i])
                    else:
                        num = num + dict_s.get(s[i])
                elif s[i] == "D":
                    num = num + dict_s.get("D")
                elif s[i] == "M":
                    num = num + dict_s.get("M")

        print('\n', "length of s =", len(s), '\n')
        print("num =", num)


sol = Solution()
sol.romanToInt('MCMII')  # I V
