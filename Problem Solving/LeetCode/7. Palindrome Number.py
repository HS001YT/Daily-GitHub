class Solution:
    def isPalindrome(self, x: int) -> bool:

        # We have two approch which differ in time and space complexities
        
        # 1) with the help of strings (Time - O(n) & Space - O(n))
        # str_num = str(x)
        # return str_num == str_num[::-1]

        # 2) with direct integer operations (Time - O(log₁₀(n)) & Space - O(1))

        if x<0 or x%10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10 (middle digit gets ignored)
        return x == reversed_half or x == reversed_half // 10
