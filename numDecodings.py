"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

# Solved using bottom up approach
# Build an array to store the values
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        arr = [0] * (n + 1)
        arr[0] = 1
        if n == 0:
            return 1
        if s[0] == '0':
            return 0
        else:
            arr[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    arr[i] = arr[i - 2]
                else:
                    return 0
            else:
                if s[i - 2] == '1' or (s[i - 2] == '2' and int(s[i - 1]) < 7):
                    arr[i] = arr[i - 2] + arr[i - 1]
                else:
                    arr[i] = arr[i - 1]

        return arr[n]
