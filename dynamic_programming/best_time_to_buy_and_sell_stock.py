class Solution:

    # DP solution
    def maxProfit(self, prices: List[int]) -> int:
        # initialize dp table
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        # dp table is a 2D array
        # dp[i][j] means the state on i-th day, there are n days in total
        # j can be 0 or 1, 0 means no stock in hand, 1 means stock in hand
        # the value of dp[i][j] is the max profit on this day with this state

        for i in range(n):
            if i == 0:
                # today is first day
                # initialize values
                dp[i][0] = 0  # net profit is 0
                dp[i][1] = -prices[i]  # Impossible to own stock now, initialize value
            else:
                # If I don't own stock today, I can either sell stock I own or do nothing
                dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
                # If I own stock today, I can either do nothing or buy stock
                # since I can only buy once, if I don't own stock previously, my profit becomes -prices[i]
                dp[i][1] = max(dp[i - 1][1], -prices[i])

        print(dp)

        return dp[n - 1][0]

    # Two pointers solution
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = 0

        left = 0
        right = 1

        while right < len(prices):
            curr_profit = prices[right] - prices[left]

            if curr_profit > 0:
                profit = max(curr_profit, profit)
            else:
                left = right
            right += 1

        return profit
