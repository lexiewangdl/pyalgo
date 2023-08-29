# 322. Coin Change
import math


class Solution:
    memo = []

    def dp(self, coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        min_n_coins = math.inf

        if self.memo[amount] != -2:
            return self.memo[amount]

        for coin in coins:
            n_coins = self.dp(coins, amount - coin)
            if n_coins != -1:
                min_n_coins = min(1 + n_coins, min_n_coins)

        self.memo[amount] = min_n_coins if min_n_coins != math.inf else -1

        return self.memo[amount]

    def coinChange(self, coins: list, amount: int) -> int:
        self.memo = [-2] * (amount + 1)
        return self.dp(coins, amount)
