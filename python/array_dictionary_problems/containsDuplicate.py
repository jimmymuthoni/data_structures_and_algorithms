from typing import List
class Solution:
    def containsDuplicate(self, nums:List[int])-> bool:
        #create the hashset to store nums
        distinct_values = set()
        #loop through thr nums 
        for num in nums:
            #check if the number is in the set
            if num in distinct_values:
                return True
            #add the num to the hashset if not found
            distinct_values.add(num)
        return False #dublicate not found

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([2,7,8,9,12,44,1,5]))

"""
Time complexity: 0(1) takes constant time to access the element in the set
0(n) worst case for going through the array till we find the num
space complexity 0(n) --> introduction of one new ds.
"""
