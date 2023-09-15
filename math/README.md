# Math Problems

## Table of Contents

- (9) Palindrome Number (Easy)

### 9. [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) (Easy)
#### Solution 1: Two pointers, Convert integer to string
Convert the input integer to a string, use two pointers, `left` initialized to be at index 0, 
and `right` initialized to be at `len(string_x)-1`.
Increment `left` and decrement `right` simultaneously until they meet. At each step, check if the
character at two indices are the same. If not, return `False`.

#### Solution 2: Maths
For integers, we can't just use indices to access digits.

However, we can reverse the input integer (just like how we reverse a string), doing the following:
- Get the one's digit of an integer using the modulus operator
- Divide number by 10 at each step, so that we can keep getting the number at one's digit

To get the number at one's digit of integer `x`, we can do `x % 10`, because the remainder when a number is divided by 10
is the number at one's digit. For example ...
```python
>>> 121 % 10
1
>>> 189 % 10
9
>>> 35472 % 10
2
```

After getting each number at one's digit, we will need to divide number by 10, to get the number at next digit.
However, `/` is float division operator. To get integer results, we need to use `//`.
```python
>>> 13.1 / 10
1.31
>>> 13.1 // 10
1.0
```

Also, if input integer is a negative number, it can't be a palindrome. Thus, we can write: `if x < 0: return False`.


