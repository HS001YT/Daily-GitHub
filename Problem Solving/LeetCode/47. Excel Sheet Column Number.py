class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Convert character to number: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
