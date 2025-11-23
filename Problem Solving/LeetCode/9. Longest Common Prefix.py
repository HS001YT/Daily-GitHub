class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # If strs is empty
        if not strs:
            return ""

        # We are going in reverse 
        prefix = strs[0]  # take the first word as initial prefix

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:  # check if prefix is at the start
                prefix = prefix[:-1]  # shorten prefix - remove last element
                if not prefix:
                    return ""
        return prefix