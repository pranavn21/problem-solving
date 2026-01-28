from typing import List

# Leetcode Problem 152: Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the maximum element (handles single element case)
        res = max(nums)
        # Track both max and min products ending at current position
        # We track min because a negative number * negative number = positive
        curr_max, curr_min = 1, 1

        for n in nums:
            # Reset both trackers when we encounter 0 (breaks the product chain)
            if n == 0:
                curr_max, curr_min = 1, 1
                continue

            # Store the previous max before updating (needed for min calculation)
            temp = curr_max * n
            # Update curr_max: either continue previous max product, use previous min (for negatives), or start fresh with n
            curr_max = max(n * curr_max, n * curr_min, n)
            # Update curr_min: either continue previous max (for negatives), use previous min, or start fresh with n
            curr_min = min(temp, n * curr_min, n)

            # Update result with the current maximum product found
            res = max(res, curr_max)

        return res

# Time complexity: O(n), where n is the number of elements in nums (single pass)
# Space complexity: O(1), only using constant extra space for variables