"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


"""

class Solution:
    def roman_to_integer(self, s:str) -> int:
        roman_numeral = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900
        }

        total = 0
        i = 0
        #process two symbols
        while i < len(s):
            if i < len(s) - 1:
                two_symbols = s[i: i+2]
                if two_symbols in roman_numeral:
                    total += roman_numeral[two_symbols]
                    i += 2
                    continue
            #process one symbol
            one_symbol = s[i]
            total += roman_numeral[one_symbol]
            i += 1
        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.roman_to_integer("MDXLIX"))


"""
space complexity: O(1)
time complexiy: O(1)
"""
