"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1]
+ arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

"""


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        sum_in_window = arr_sum / 3
        curr_sum = 0
        count = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if count < 2:
                if curr_sum == sum_in_window:
                    count += 1
                    curr_sum = 0
                    if i == len(arr) - 1:  # if we have less than 2 windows and on the last item in array, False
                        return False
            if count == 2 and sum(arr[i:]) == sum_in_window:
                return True
        return False
