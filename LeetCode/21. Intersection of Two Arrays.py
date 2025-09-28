class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # use set for uniqueness and O(1) lookup
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)  # intersection of sets
