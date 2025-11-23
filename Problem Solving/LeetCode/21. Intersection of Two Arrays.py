# Intersection means returning the common elements between the two lists

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # First make the lists with only unique values
        set1 = set(nums1)
        set2 = set(nums2)

        # Now return the common elements in sets by forming list of them by using and (&).
        return list(set1 & set2)
