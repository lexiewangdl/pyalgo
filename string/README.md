# String Problems

## Table of Contents 
- 🚩 [2232. Minimize Result by Adding Parentheses to Expression](#2232-minimize-result-by-adding-parentheses-to-expression--medium-) 🍊

## String Manipulation Tricks
- Find the index of a character in a string: `expression.find('c')`
  ```python
  >>> "33+55".find('+')
  2
  ```
- Evaluate the numerical value of a mathematical expression: `eval(expression)`
  ```python
  >>>   eval("121*(1+2)")
  363
  ```


### [2232. Minimize Result by Adding Parentheses to Expression](https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description/) (Medium)
The input expression can be split into four parts by adding a pair of parentheses:
- The expression becomes `a(b+c)d` after adding parentheses
- The four parts are `a`, `b`, `c`, and `d`
- Edge case: `a` and `d` can be empty strings

**Approach**: two pointers (with nested `for` loops)
- Why two for loops? This is because we need to consider all possible ways to split the expression into four parts. For example, if the expression is `123+45`, the left part can be split into `(123`, `1(23`, `12(3`, and the right part can be split into `4)5` and `45)`. We must evaluate all possible **combinations**.
- Find the index of '+' with `plus_idx = expression.find('+')`
- Two pointers: `left` is the index where we insert the left parenthesis, `right` is the index where we insert the right parenthesis
- For loop (left part): `for left in range(0, plus_idx)`, `left` can take any value from 0 to `plus_idx - 1` (inclusive)
- For loop (right part): `for right in range(plus_idx + 2, len(expression) + 1)`. This is because, for `right` to be the index where we insert the right parenthesis, it must be at least 2 characters away from `plus_idx`. Also, `right` can take any value from `plus_idx + 2` to `len(expression)` (inclusive). `right` can be equal to `len(expression)` because the right parenthesis can be at the end of the string.
- Use string slicing to get three substrings: `a`, `b+c`, and `d`
- `a` is `expression[:left]`, but if `left` is 0, `a` is an **empty string**, in this case, we want to replace it with `1`
- `b+c` is `expression[left: right]`
- `d` is `expression[right:]`, but if `right` is `len(expression)`, `d` is an **empty string**, in this case, we want to replace it with `1`
- Concatenate the three substrings into a new expression: `new_expression = a + '*(' + b + '+' + c + ')*' + d`. We must include the `*` signs here, because we want to evaluate the expression as a mathematical expression, not a string.
- Check whether `eval(new_expression)` is smaller than `min_val`, if so, update `min_val`.
- Return the expression that gives the smallest result. This will be `expression[:left] + '(' + expression[left: right] + ')' + expression[right:]` (no need to take care of the edge case here, because in those cases, the parts to the left and right of parentheses will be empty string)

**Time complexity**: O(n^2)


