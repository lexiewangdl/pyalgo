# 121.

class Solution:
    import math

    # DP Solution
    def maxProfit(self, prices: List[int]) -> int:
        num_days = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        for i in range(num_days):
            # initialize values for the first day
            if i == 0:
                dp[i][0] = 0  # own no stock, then profit is 0
                dp[i][1] = -prices[i]  # bought on first day
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[
                    i])  # no stock, either I bought stock and sold it, or I never bought
                # I can only buy once, so if I choose to buy today, then my net profit is -prices[i]
                dp[i][1] = max(-prices[i], dp[i - 1][
                    1])  # own stock, either I didn't have stock & bought today or I already have bought

        return dp[num_days - 1][0]
