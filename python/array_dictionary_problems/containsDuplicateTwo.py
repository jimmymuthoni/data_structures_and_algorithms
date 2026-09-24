#hashmap solution
from typing import List
class Solution:
    def containsNearbyDuplicateTwo(self,nums:List[int], k:int)->bool:
        num_idx = {} #stores number and the last index num was seen
        for i in range(len(nums)):
            if nums[i] in num_idx:
                if abs(num_idx[nums[i]] - i) <= k:
                    return True
            num_idx[nums[i]] = i
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicateTwo([1,2,3,4,1], 3))


"""
Given an integer array nums and an integer k, return true if there are two
distinct indicies i and j in the array such that nums[i] == nums[j] and 
abs(i -j) <= k
Time complexity 0(n)
Space complexity O(k)

"""

#hashset solution
class Solution:
    def containsNearbyDuplicate(self, nums:List[int], k:int) -> bool:
        num_set = set()
        for i, num in enumerate(nums):
            #if num ia alreay in the wwindow, duplicate found
            if num in num_set:
                return True
            #add current number
            num_set.add(num)
            #keep only the last k elements
            if len(num_set) > k:
                num_set.remove(num[i - k])
        return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 4, 1], 4))
