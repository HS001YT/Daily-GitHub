class Solution:
    def strStr(self, string: str, substring: str) -> int:
        # change str names to string, substring
        
        if substring in string:
            n = len(string)
            m = len(substring)
            for i in range(n):
                j = 0
                for k in range(i, n):
                    if string[k] == substring[j]:
                        j += 1
                    else:
                        break
                    if j == m:
                        return i
            # k iterates in the main string
            # j iterates in the substring

        else:
            return -1

# Built - in function for this
# return string.find(substring)