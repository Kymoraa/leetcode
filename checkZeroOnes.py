"""
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest
contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of
0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
The same applies if there is no 1's.


Example 1:
Input: s = "1101"
Output: true

Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Runtime: 40 ms, faster than 64.15% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
Memory Usage: 14 MB, less than 16.23% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = s.split('0')
        zeros = s.split('1')
        max_len_1 = 0
        max_len_0 = 0

        for i in ones:
            len_one = len(i)
            max_len_1 = max(max_len_1, len_one)

        for j in zeros:
            len_zeros = len(j)
            max_len_0 = max(max_len_0, len_zeros)

        return max_len_1 > max_len_0
