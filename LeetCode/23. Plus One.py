class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):   # iterate backwards

            if digits[i] == 9:  # Checks last digit is 9?
                digits[i] = 0
            else:               # Not 9, then simply add 1
                digits[i] += 1
                return digits

        # This return works when loop end with if only i.e, all were 9s
        return [1] + [0] * len(digits)