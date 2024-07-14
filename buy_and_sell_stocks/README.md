

## Table of Contents
- [Overview](#overview)
- [Buy and Sell Once](#buy-and-sell-once)

## Overview

The DP table needs to have the following dimensions:
- Day (`i`)
- Number of transactions left (`k`)
- Current state (`0` for not holding, `1` for holding)

The goal is to find `dp[n-1][k][0]` where `n-1` is the index of last day.

The base cases are:
- `dp[-1][..][0] = 0` (no buying on the first day)
- `dp[-1][..][1] = -math.inf` (buying on the first day, profit is the cost)
- `dp[..][0][0] = 0` (no transactions left, thus no profit)
- `dp[..][0][1] = -math.inf` (no transactions left, thus no profit)

DP formula:
```python
# not holding stock
# (1) yesterday, k transactions left, had no stock, no action today
# (2) yesterday, k transactions left, held stock, sold today
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])

# holding stock
# (1) yesterday, k-1 transactions left, had no stock, buy in today
# (2) yesterday, k transactions left, held stock, no action today
dp[i][k][1] = max(dp[i-1][k-1][0] - prices[i], dp[i-1][k][1])
```

## Buy and Sell Once
[121. Best Time to Buy and Sell Stock ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**How to initialize the base case values of DP table?**
- `dp[0][0] = max(dp[-1][0], dp[-1][1] + prices[i])`, which would be `0`, since the latter is negative infinity.
- `dp[0][1] = max(dp[-1][0] - prices[i], dp[-1][1])`, which would be `-prices[i]` (buy on first day), since latter is negative infinity.

## Cooldown Period
[309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

There are two base case situations: (1) when `i == 0` and (2) when `i == 1`.
Modify the formula based on cooldown restriction:
```python
dp[1][1] = max(-prices[i], dp[i-1][1]) # on 1st day (not 0-th), can only buy for the first time due to cooldown

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-2][0] - prices[i], dp[i-1][1]) # cooldown
```



