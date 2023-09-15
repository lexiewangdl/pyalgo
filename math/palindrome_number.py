class Solution:

    # without converting integer to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        y = 0

        while temp > 0:
            num = temp % 10
            temp = temp // 10
            y = 10 * y + num

        return y == x

    # Two pointers solution
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1

        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1

        return True