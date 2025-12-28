from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store the numbers we have seen so far, O(1) lookup time
        seen = {} # Key: nums[index]; Value: index

        # Iterate through the list of numbers, we need to track the index
        for index, num in enumerate(nums):
            need = target - num # Calculate the target
            if (need) in seen: # If we have seen the needed number before
                return [seen[need], index] # Return the indices
            seen[num] = index # Otherwise, store the number with its index

        return []  # Return an empty list if no solution is found

# Time complexity: O(n), where n is the number of elements in nums
# Space complexity: O(n) for the hash map storing seen numbers