from typing import List
class Solution:
    def two_sum(self, nums:List[int], target:int)->List[int]:

        #dictionarry to store numbers and their indices
        hashmap = {}

        #loop through the array
        for i, num in enumerate(nums):
            #get diffreence
            diff = target - num

            #check if the diffrence is in hashmap
            if diff in hashmap:
               return[hashmap[diff], i]

            #add to hashmap if not found
            hashmap[num] = i
        return []
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([11,7,2,15],9))


#  time complexity: O(n)
#  space complexity: O(n)