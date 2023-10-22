import math


class Solution:
    def minimizeResult(self, expression: str) -> str:
        ans = (math.inf, expression)

        # find index of '+'
        plus_idx = expression.find('+')

        # two pointers, [l, r)
        for l in range(0, plus_idx):
            left = expression[:l] if expression[:l] else "1"

            for r in range(plus_idx + 2, len(expression) + 1):  # 右边是开区间
                mid = expression[l:r]
                right = expression[r:] if expression[r:] else "1"
                curr_exp = left + "*(" + mid + ")*" + right
                if eval(curr_exp) < ans[0]:
                    ans = (eval(curr_exp), expression[:l] + '(' + mid + ')' + expression[r:])

        return ans[1]
