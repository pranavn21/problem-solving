from typing import List

# Leetcode Problem 121: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max profit to 0, since we can choose not to trade
        maxProfit = 0
        # Two pointers: left = buy day, right = sell day
        left, right = 0, 1
        
        # Iterate through all possible sell days
        while right < len(prices):
            # Check if this is a profitable transaction
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]  # Calculate current profit
                maxProfit = max(profit, maxProfit)  # Update max profit if current is higher
            else:
                # Found a lower price, move buy pointer to this day
                left = right

            right += 1  # Move sell pointer to next day

        return maxProfit  # Return the maximum profit found

# Time complexity: O(n), where n is the number of elements in prices (single pass)
# Space complexity: O(1), only using constant extra space for variables     