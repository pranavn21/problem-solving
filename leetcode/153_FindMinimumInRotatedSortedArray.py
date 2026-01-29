from typing import List

# Leetcode Problem 153: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element (handles single element case)
        res = nums[0]
        l, r = 0, len(nums) - 1

        # Binary search for the minimum in the rotated sorted array
        while l <= r:
            # If the current subarray is sorted, the leftmost element is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            # Consider middle as a candidate for the minimum
            res = min(res, nums[m])

            # If the left half is sorted, the minimum must be in the right half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Otherwise, the minimum is in the left half
                r = m - 1

        return res

# Time complexity: O(log n) where n is the length of nums (binary search)
# Space complexity: O(1), only constant extra space used