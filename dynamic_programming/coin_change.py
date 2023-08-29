# 322. Coin Change
import math

# Bottom-up approach
class Solution:
    memo = []

    def coinChange(self, coins, amount) -> int:
        self.memo = [-2] * (amount + 1)
        self.memo[0] = 0

        for i in range(1, amount + 1):
            print(f"Amount: {i}", self.memo)

            n_coins = math.inf
            for coin in coins:
                # if i-coin is out of range, or
                # if summing to i-coin is impossible
                if i - coin >= 0 and self.memo[i - coin] != -1:
                    n_coins = min(1 + self.memo[i - coin], n_coins)
                    print(f"Coin: {coin}", " Num coins: ", n_coins)

            self.memo[i] = n_coins if n_coins != math.inf else -1

        return self.memo[amount]


# Top-down approach
# class Solution:
#     memo = []
#
#     def dp(self, coins, amount):
#         if amount < 0:
#             return -1
#         if amount == 0:
#             return 0
#
#         min_n_coins = math.inf
#
#         if self.memo[amount] != -2:
#             return self.memo[amount]
#
#         for coin in coins:
#             n_coins = self.dp(coins, amount - coin)
#             if n_coins != -1:
#                 min_n_coins = min(1 + n_coins, min_n_coins)
#
#         self.memo[amount] = min_n_coins if min_n_coins != math.inf else -1
#
#         return self.memo[amount]
#
#     def coinChange(self, coins: list, amount: int) -> int:
#         self.memo = [-2] * (amount + 1)
#         return self.dp(coins, amount)

if __name__ == "__main__":
    s = Solution()
    # s.coinChange([1, 2, 5], 11)
    s.coinChange([2], 3)

