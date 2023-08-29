# Dynamic Programming
**Table of Contents**
- 509 Fibonacci Number
- 322 Coin Change

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


