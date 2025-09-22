class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

# Another Faster approch

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for x in nums:
#             if x in seen:
#                 return True
#             seen.add(x)
#         return False
