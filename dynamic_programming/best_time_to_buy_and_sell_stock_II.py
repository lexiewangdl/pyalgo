# 122. Best Time to Buy and Sell Stock II
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # initialize dp table
        dp = [[0 for _ in range(2)] for _ in range(n)]

        for i in range(n):
            if i == 0:
                # initialize dp values
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0] if dp[n-1][0] > 0 else 0
