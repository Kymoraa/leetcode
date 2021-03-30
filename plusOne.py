"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # converting the int list into a string, then into an integer for easy addition.
        # Then converting the result back into a list of integers
        digits = [str(i) for i in digits]
        digits = int(''.join(digits))
        digits = digits + 1
        return [int(x) for x in str(digits)]


"""
The solution above is a bit crude...
Converting inputs to different formats et al.
Below is a better implementation using an iterative solution

"""


def plusOne(input_array):
    carry = 1
    n = len(input_array)
    new_array = [0] * n

    for i in range(n-1, -1, -1):
        sum = input_array[i] + carry
        if sum == 10:
            carry = 1
        else:
            carry = 0
            new_array[i] = sum % 10
    if carry == 1:
        new_array = [0] * (n+1)
        new_array[0] = 1
    return new_array
