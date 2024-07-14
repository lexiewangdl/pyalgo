

## Table of Contents
- [Overview](#overview)
- [One or Infinite Transactions](#one-or-infinite-transactions)
- [Cooldown Period](#cooldown-period)
- [Transaction Fee](#transaction-fee)
- [Transaction Limit](#transaction-limit)

## Overview

The DP table needs to have the following dimensions:
- Day (`i`)
- Number of transactions (`k`)
- Current state (`0` for not holding, `1` for holding)

The goal is to find `dp[n-1][k][0]` where `n-1` is the index of last day.

The base cases are:
- `dp[-1][..][0] = 0`, before trading session, net profit is 0.
- `dp[-1][..][1] = -math.inf`, before trading session, impossible to hold stock.
- `dp[..][0][0] = 0`, no transaction, net profit is 0.
- `dp[..][0][1] = -math.inf`, no transaction, impossible to hold stock.

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

## One or Infinite Transactions
- [121. Best Time to Buy and Sell Stock ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

When `k == 1` or `k == inf`, there is no need to keep track of `k`. The DP formula is simple, just remove `k`.

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

## Transaction Fee

[714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)

Modify the DP formula to include transaction fee:
```python
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
```

## Transaction Limit
[123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/)

- Use the [general DP formula](#overview) above.
- Use nested `for` loops:
  - The outer loop is `for i in range(num_days):`
  - The inner loop is `for k in range(1, max_k):`, we don't process instances where `k < 1`, i.e. when no transaction left, value is always 0 as when `dp` table is initialized.
- Return `dp[num_days-1][max_k][0]`, net profit on last day, max number of transactions.



