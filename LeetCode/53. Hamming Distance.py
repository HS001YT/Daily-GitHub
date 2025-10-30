class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR to find differing bits, then count the number of 1s
        return bin(x ^ y).count('1')
