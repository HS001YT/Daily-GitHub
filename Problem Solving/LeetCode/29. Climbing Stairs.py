class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        a, b = 1, 1  # a = dp[i-2], b = dp[i-1]

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

        # Example
        print(climbStairs(5))  # Output: 8