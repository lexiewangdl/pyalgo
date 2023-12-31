# Math Problems

## Table of Contents

- 9 - Palindrome Number (Easy)
- 303 - Range Sum Query - Immutable (Easy)
- 304 - Range Sum Query 2D - Immutable (Medium)
- [311. Sparse Matrix Multiplication](#311-sparse-matrix-multiplication--medium-) (Medium)
- [268. Missing Number](#268-missing-number-easy) (Easy)

### 9. [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) (Easy)
#### Naive Solution: Two pointers, Convert integer to string
Convert the input integer to a string, use two pointers, `left` initialized to be at index 0, 
and `right` initialized to be at `len(string_x)-1`.
Increment `left` and decrement `right` simultaneously until they meet. At each step, check if the
character at two indices are the same. If not, return `False`.

#### Better Solution: Maths
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

### 303. [Range Sum Query - Immutable ](https://leetcode.com/problems/range-sum-query-immutable/description/)(Easy)

#### Naive Solution
Every time there is a query, just iterate through every number from index `left` to `right` (inclusive), and add them up.
Time complexity is O(n), space complexity is O(1).

#### Quick Solution
Use a 1D array `memo` or `preSum`, which stores the sum of all numbers from index 0 up to this index (inclusive).
```bash
     nums = [1, 2, 3,  4,  5]
preSum = [0, 1, 3, 6, 10, 15]
```
Thus, `preSum[i]` stores the sum of all values from `nums[0]` to `nums[i-1]` inclusive.

How to fill in this array `preSum`? `preSum[i] = preSum[i-1] + nums[i]`. The first value is always initialized to be 0, becuase
the sum of all numbers in `nums` array before index 0 is always 0.

### 304. [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/description/) (Medium)
The 2D array `memo` stores at (x+1, y+1) the area of rectangle with the origin (0, 0) as top-left corner, and (x, y) as bottom-right
corner (where x and y are coordinates in `matrix`).

For ease of calculation, `memo`'s size will be `len(matrix)+1, len(matrix[0])+1`, and the first row and first column 
will be initialized to be 0.

**Initializing memo**:
```bash
# Matrix
[[3, 0],
 [5, 6]]
 
# Memo
[[0, 0, 0],       [[0, 0, 0],
 [0, 3, 0],  -->   [0, 3, 3],  
 [0, 0, 0]]        [0, 8, ?]]
 
 ? = 8 + 3 - 2 + 6 = 14
```
For example, given the 2 by 2 matrix above ...
- Initialize `memo` of size (2+1, 2+1), first row and first col are all zeroes
- Starting from index `(1,1)`, fill in the number
- How to find the value at `memo[i][j]` given that previous cells have been filled?
- `memo[i][j] = memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1] + matrix[i-1][j-1]`, where ...
  - `memo[i-1][j]` is the cell immediately on top of current cell we are trying to fill
  - `memo[i][j-1]` is the cell to the left
  - Since both of these cell values were determined by summing `memo[i-1][j-1]` and the matrix value corresponding to their position, `memo[i-1][j-1]` (top left cell) needs to be subtracted
  - Finally, add `matrix[i-1][j-1]`, which is this cell's corresponding cell in matrix

**Query:**
Simply access values from `memo` and do subtraction and addition accordingly.
![Example](https://labuladong.github.io/algo/images/%E5%89%8D%E7%BC%80%E5%92%8C/5.jpeg)

### 311. [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/description/) (Medium)

**矩阵乘法**：
- 矩阵点乘：矩阵A和B的size必须一样，对应位置的元素相乘
- 矩阵叉乘：矩阵A✖️B，A的列数必须等于B的行数，结果矩阵的size是A的行数和B的列数

A (l x m) ✖️ B (m x n) = C (l x n)

![Matrix Multiplication](https://www.geeksforgeeks.org/wp-content/uploads/strassen_new.png)

**Python solution**
用三个nested for loops，第一层和第二层for loop分别遍历结果矩阵R的每一行和每一列。第一层for loop为
`for l in range(len(A))`，第二层for loop为`for n in range(len(B[0]))`。第三层for loop为`for m in range(len(A[0]))`，
这样的话，在每一步更新`R[l][n]`的时候，就可以用`R[l][n] += A[l][m] * B[m][n]`。

**Time Complexity:** O(lmn)

**NumPy solution:**
- Initialize array from list of list: `A = np.array(matrix1)`
- Matrix multiplication: `R = matmul(A, B)`
- Result: `R.tolist()`
- Simplified: `matmul(np.array(mat1), np.array(mat2)).tolist()`


### 268. [Missing Number](https://leetcode.com/problems/missing-number/description/) (Easy)

**My approach:** 

Sort the array in ascending order using `array.sort(revers=False)`. Initialize `ans = 0`. 
Iterate through the array, if the current number is not equal to `ans`, return `ans`. 
Otherwise, increment `ans` by 1. If the loop finishes, return `ans`.

**Mathematical approach:**

Calculate the expected sum of all integers within the range `[0, N]`, where `N` is the length of the array.
Then calculate the actual sum of all integers in the array. 
The difference between the expected sum and the actual sum is the missing number.

