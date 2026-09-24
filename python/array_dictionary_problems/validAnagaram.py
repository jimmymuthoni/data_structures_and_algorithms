"""
Given two strings s and t, return true if it is an anagram of s, and false otherwise
anagram every character present in s is also present in t
"""

class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        #check if the length of characters are same
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1 #count how mnay tims each character appears

        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] < 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))      
        
"""
Space complexity O(k) k> number of distict characters k <= 26
Time O(n) > n length of the string
"""

           