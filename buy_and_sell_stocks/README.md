

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
- `dp[-1][k][0] = 0` (no buying on the first day)
- `dp[-1][k][1] = -prices[i]` (buying on the first day, profit is the cost)
- `dp[i][0][0] = 0` (no transactions left, thus no profit)
- `dp[i][0][1] = -infinity` (no transactions left, thus no profit)

## Buy and Sell Once
[121. Best Time to Buy and Sell Stock ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
