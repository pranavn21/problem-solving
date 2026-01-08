from typing import List

# Leetcode Problem 217: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a hash set to track numbers we've already seen
        # Sets provide average O(1) lookup and insert
        seen = set()

        # Scan through the array once
        for n in nums:
            # If we've seen n before, we found a duplicate
            if n in seen:
                return True

            # Otherwise, record n as seen
            seen.add(n)

        # If we finish the loop, no duplicates were found
        return False

# Time complexity: O(n), where n is the number of elements in nums (single pass)
# Space complexity: O(n) in the worst case, when all elements are unique