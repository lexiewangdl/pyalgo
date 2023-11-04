# 38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"

        # get the output of n-1, i.e. the digit string output of countAndSay(n-1)
        prev = self.countAndSay(n - 1)

        # how to say this string
        result = ""
        curr_d = prev[0]
        count = 1

        for i in range(1, len(prev)):
            if prev[i] != curr_d:
                result += (str(count) + curr_d)
                curr_d = prev[i]
                count = 1
            else:
                count += 1

        # append final sequence to result
        result += (str(count) + curr_d)
        return result
