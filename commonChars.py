"""Given a string array words, return an array of all characters that show up in all strings within the words (
including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Runtime: 104 ms, faster than 14.73% of Python3 online submissions for Find Common Characters.
Memory Usage: 14 MB, less than 55.81% of Python3 online submissions for Find Common Characters.
"""


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        first_word = words[0]
        if len(words) == 1:
            return list(first_word)
        output = []
        words = [list(i) for i in words[1:]]
        count = 0
        for i in first_word:
            for j in range(len(words)):
                if i in words[j]:
                    words[j].remove(i)
                    count += 1
            if count == len(words):
                output.append(i)
            count = 0
        return output
