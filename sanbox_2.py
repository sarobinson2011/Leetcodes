# Sandbox for solution to leetcode #12 - romanToInteger
class Solution:
    def intToRoman(self, num: int) -> str:
        # Map the Roman numerals to their corresponding decimal value
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
