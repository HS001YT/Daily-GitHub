class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        result = []
        
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:  # char == 'D'
                result.append(high)
                high -= 1
        
        # Append the last remaining number
        result.append(low)  # low == high here
        return result
