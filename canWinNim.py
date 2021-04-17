"""
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.

Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play
optimally, otherwise return false.

Almost similar to the #divisorGame, the only way the first player will win is if on their turn the number n, is not
divisible by 4. i.e. On the final round their turn is not a heap of 4 stones. Because regardless of how they play, they
will lose

"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
