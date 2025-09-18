from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # We have two approch to solve this problem
        # 1) Sort both string then return the comparing result
        # return sorted(s) == sorted(t)
        # But this approch has Time - O(n log₁₀ n) and Space - O(n) in python as it creates a new list

        # 2) Incresing the counter which is lighter then the sorting
        # counter of 26 alphabets which gives Time - O(n) and Space - O(1)
        return Counter(s) == Counter(t)
