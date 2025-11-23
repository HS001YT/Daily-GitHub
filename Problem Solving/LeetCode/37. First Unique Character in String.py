class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character
        count = Counter(s)
        
        # Find the first character with frequency 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1
