"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


"""
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k:int):
        if k == len(nums):
            return nums
        
        count = {}
        # Count frequencies
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Min heap
        heap = []

        # Keep only k elements
        for n in count:
            heapq.heappush(heap, (count[n], n))

            if len(heap) > k:
                heapq.heappop(heap)

        # Get results
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))

"""
Time: O(n log k)

Space: O(n) 
"""