from typing import List

# Leetcode Problem 53: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub with the first element
        # This ensures we have a valid starting point
        maxSub = nums[0]
        # Running sum of the current subarray
        currSum = 0

        # Iterate through all numbers using Kadane's algorithm
        for num in nums:
            # If current sum becomes negative, reset it to 0
            # Because adding a negative number to future elements will only decrease them
            if currSum < 0:
                currSum = 0
            # Add current number to the running sum
            currSum += num
            # Update maxSub if current sum is greater
            maxSub = max(maxSub, currSum)
        
        return maxSub

# Time complexity: O(n), where n is the number of elements in nums (single pass)
# Space complexity: O(1), only using constant extra space for variables