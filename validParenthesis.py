"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        # define opening and closing brackets. Ensure the indices of the pairs are the same in the two lists.
        open_braces = ["[", "{", "("]
        close_braces = ["]", "}", ")"]
        stack = []
        for i in s:
            if i in open_braces:
                stack.append(i)
            elif i in close_braces:
                pos = close_braces.index(i)
                if (len(stack) > 0) and (open_braces[pos] == stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

