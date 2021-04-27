"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Took a very random kind of route... where I found the square root and converted the value to an int then squared it
again.

Found a solution that's probably better using binary search.
Use that one lol.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True

        high = num
        low = 1

        while low <= high:

            mid = (high + low) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            elif sq < num:
                low = mid + 1
        return False
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        return int(num ** 0.5) ** 2 == num
