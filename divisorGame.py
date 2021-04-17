"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

My thoughts:
1. Alice is playing first
2. Thus the only way Alice can win is if the n value is an even number. Because of the constraints set of choosing x as
0 < x < n and n % x == 0

N.B. The players are playing the game optimally to ensure they win

"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
