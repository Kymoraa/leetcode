"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Time complexity = O(amount * len(coins))
Space complexity = O(amount + 1) for the dp cache
"""
import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0  # base case since no coins are needed to make an amount of 0

        for coin in coins:
            # start from coin; you can't make an amount less than coin using that coin
            for amt in range(coin, amount + 1):
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)  # 1 accounts for using one more coin.
        return -1 if dp[amount] == math.inf else dp[amount]
