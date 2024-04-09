# 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]

        current_length = 0
        for i in range(len(s)):
            # If current element is opening parenthesis, push index to stack
            if s[i] == '(':
                stack.append(i)

            # If current element is closing parenthesis,
            else:
                stack.pop() # pop top element
                if len(stack) == 0: # if stack is empty after pop
                    stack.append(i) # append current index
                else:
                    # stack[-1] is the index of last un-matched element
                    # i-stack[-1] is length of valid substring
                    max_length = max(max_length, i-stack[-1])

        return max_length