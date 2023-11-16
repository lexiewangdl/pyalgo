# Dynamic Programming
**Table of Contents**
- Buying and Selling Stocks
  - [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock-easy) 🍏
  - [122. Best Time to Buy and Sell Stock II](#122-best-time-to-buy-and-sell-stock-ii-medium) 🍊
- Uncategorized
  - [509. Fibonacci Number](#509-fibonacci-number-easy) 🍏
  - [322. Coin Change](#322-coin-change-medium) 🍊

## Buying and Selling Stocks

### Summary

### 121. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) (Easy)
使用一个dp table来存储在每一天，持有和不持有股票的情况下，最大的利润是多少。最后返回dp table中最后一天，不持有股票的情况下的最大利润。
因为这道题中`k`（交易次数）并不是一个变量，而是固定的`k=1`，所以可以使用一个2D dp table，`dp[i][0]`代表第`i`天不持有股票的最大利润，
`dp[i][1]`代表第`i`天持有股票的最大利润。`0`和`1`是不同的**状态**。

接下来需要思考的是状态如何转移。

假设今天是第`i`天，那么今天不持有股票的最大利润有两种情况：
(1) 昨天不持有股票，今天也不持有股票，即`dp[i][0] = dp[i-1][0]`
(2) 昨天持有股票，今天卖出了股票，即`dp[i][0] = dp[i-1][1] + prices[i]`

今天持有股票的最大利润也有两种情况：
(1) 昨天持有股票，今天也持有股票，即`dp[i][1] = dp[i-1][1]`
(2) 昨天不持有股票，今天买入了股票，即`dp[i][1] = dp[i-1][0] - prices[i]`，
但是因为这道题中只能进行一次交易，所以`dp[i][1] = -prices[i]`（也就是买入股票之前最大利润必定是0），如果交易次数不限，那就可以用原式子。

接下来还需要考虑dp table如何 initialize，第一天`i=0`时，不持有股票的最大利润为0，持有股票的最大利润为`-prices[0]`。
这是因为第一天如果持有股票，那么必定是在第一天买入了股票，所以最大利润为`-prices[0]`。

Example:
```python
prices = [7, 1, 5, 3, 6, 4]
```

Initialize dp table, at this time, only initialize the first row, which is when `i=0`:
```python
dp = [[0, -7],  # day 0
      [0, 0],  # day 1
      [0, 0],  # day 2
      [0, 0],  # day 3
      [0, 0],  # day 4
      [0, 0]]  # day 5
```

Fill in the rest of the dp table:
```python
dp = [[0, -7],  # day 0，不买股票的话利润为0，买了股票利润为-7
      [0, -1],  # day 1，不持有股票状态，要么利润和昨天不持有股票一样为0，要么是买了股票又卖了，就是-7+1=-6，选择0
                # 持有股票状态，要么利润和昨天持有股票一样为-7，要么是昨天不持有股票，今天买入了，就是0-1=-1，选择-1
      [4, -1],  # day 2， 不持有股票状态，可以卖掉手里的股票，也就是-1+5=4，也可以不持有股票，利润和昨天一样为0，选择4
                # 持有股票状态，可以选择和昨天一样持有股票，利润为-1，也可以选择买入股票，利润为0-5=-5，选择-1
      [4, -1],  # day 3
      [5, -1],  # day 4
      [5, -1]]  # day 5
```

最后返回dp table中最后一天，不持有股票的最大利润，即`dp[n-1][0] = 5`（最后一天把股票卖了肯定比不卖利润要高）。

### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/) (Medium)

注意这道题中`k`（交易次数）是不限制的，但是同一时间只能持有1支股票。

和上一道题用同样的方法，只是有一点不同，也就是当第`i`天是持有股票的状态时，`dp[i][1]`的值是多少。
`dp[i][1]`的选择有两种，要么就是前一天也持有股票，今天没有卖出，也就是`dp[i-1][1]`。或者前一天不持有股票，
今天选择买入股票`dp[i-1][0] - prices[i]`，也就是上一道题中说到的不限制交易次数的情况。


### 509. Fibonacci Number (Easy)
Given two base cases `f(0) = 0` and `f(1) = 1`, we know that for all other values of `n`, `f(n) = f(n-1) + f(n-2)`.
Thus, we know that the value of `f(n)` only depends on the values `f(n-1)` and `f(n-2)`.

Store the value of these two numbers, update at every step (after current f(n) has been calculated). No need to use an array
to store all numbers that we calculated in previous steps.

Time complexity: O(n), Space complexity: O(1)

### 322. Coin Change (Medium)
**My solution 1: Top-down approach**

This question can be solved using a dynamic programming approach because this problem can be broken down
into sub-problems of the same type as the main problem. 

- Base case: (1) when amount is equal to 0, min number of coins is 0, (2) when amount is less than 0, it's impossible, min number of coins is -1
- We have unlimited coins, as we solve the problem, `amount` will get closer to zero or negative (the base cases)
- Recursive helper method `dp()` takes two arguments: 
  - (1) `memo`, an array that keeps track of the minimum number of coins that sum up to value `k` at `memo[k]`
  - (2) `amount`, the amount that we want to find solution for, which changes as we call the recursive helper method
- `dp()` returns the minimum number of coins needed to sum up to `amount`, if impossible, return `-1`
- At each step (with each call of recursive helper function), what needs to be done?
  - Iterate over possible solutions at this step to find the ideal solution
  - At each step, we have a list of coins to choose from
  - After choosing a coin, the remainder value will be `amount - coin`
  - The minimum number of coins needed to sum up to this value is returned by `dp(amount-coin)`
  - Thus, at each step, we can do:
```python
min_num_of_coins = math.inf
for coin in coins:
    num_coins = 1 + dp(memo, amount-coin)
    min_num_of_coins = min(min_num_of_coins, num_coins)
```
- If we don't use `memo` to note down previously calculated values, there will be a lot of redundant calculations
- After every calculation, update corresponding value in `memo`

**My solution 2: Bottom-up approach**

Instead of recursively calling `dp()`, we can also build the `memo` table bottom-up, starting by filling the value of base case, which would be
`memo[0] = 0`

For any number of amount within the range `1 <= i <= amount`, find the minimum number of coins needed to sum up to amount `i`.
This is done by iterating over all possible coins, and finding the minimum value `1 + memo[i-coin]` for coin in coins.

A couple of conditions to take care of:
- If `i - coin < 0`, it's impossible to use this coin at this time
- If `memo[i-coin] == -1`, it's impossible to use our coins to sum up to value `i-coin`, thus, we can't use this value for calculation
- If the two conditions above are met, skip operations for this coin with this amount
- At the end of the for loop, if `n_coins = math.inf`, it means that none of the coins can be used at this stage, it's impossible to find a combination of coins that sum up to this amount. Set `memo[i]` to `-1`


