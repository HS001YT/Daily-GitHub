class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Using the sum formula for first n natural numbers
        total = n * (n + 1) // 2
        return total - sum(nums)
