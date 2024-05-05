# 121. Best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        # If there's only one day, no transaction can be made
        if len(prices) <= 1:
            return max_profit

        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)

            # Shrink the window:
            # If the sell price is lower than buy price, update the buy price and make it the sell price
            if prices[sell] < prices[buy]:
                buy = sell

            # Enlarge the window
            sell += 1

        return max_profit
