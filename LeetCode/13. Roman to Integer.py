class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        
        integer = 0         # Add or subtract the values in this by traversing from left to right
        n = len(s)

        for i in range(n):
            if i < n - 1 and values[s[i]] < values[s[i + 1]]:       # i < n - 1 is used to avoid IndexError as for the last 
                integer -= values[s[i]]                         # element it also search for n index which results in out of range
            else:
                integer += values[s[i]]
        
        return integer
