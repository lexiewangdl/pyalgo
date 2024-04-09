# 20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        stack = []

        for i in range(len(s)):
            # If current element is an opening bracket, add it to stack
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            # If the current element is a closing bracket,
            # compare it with the last opening bracket in stack
            else:
                # If the stack is empty (meaning that we have never encountered an opening bracket),
                # expression is invalid
                if len(stack) == 0:
                    return False

                # Check if pairing is correct
                if (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    # Invalid expression if paired incorrectly
                    return False

        return len(stack) == 0