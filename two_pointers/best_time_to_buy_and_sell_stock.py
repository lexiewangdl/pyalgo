# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = 0

        left = 0
        right = 1

        while right < len(prices) and right > left:
            curr_profit = prices[right] - prices[left]

            if curr_profit > 0:
                profit = max(curr_profit, profit)
            else:
                left = right
            right += 1

        return profit