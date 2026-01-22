from typing import List

# Leetcode Problem 238: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s
        # res[i] will store the product of all elements except nums[i]
        res = [1] * len(nums)

        # First pass: left to right
        # res[i] stores the product of all elements to the LEFT of index i
        prefix = 1  # Running product from the left
        for i in range(len(nums)):
            res[i] = prefix  # Store product of all elements before i
            prefix *= nums[i]  # Update prefix for next iteration

        # Second pass: right to left
        # Multiply res[i] by the product of all elements to the RIGHT of index i
        postfix = 1  # Running product from the right
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply by product of all elements after i
            postfix *= nums[i]  # Update postfix for next iteration

        return res

# Time complexity: O(n), where n is the number of elements in nums (two passes through the array)
# Space complexity: O(1), not counting the output array (only using constant extra space for prefix and postfix)