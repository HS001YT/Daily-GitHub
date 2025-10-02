class Solution:
    def plusOne(self, digits: list[int]) -> List[int]:
        if digits[len(digits) - 2] == 9:

            # It is not working for [9,9] make a for loop backward that continously checks for 9 in end and then use the conditions again

            if len(digits) == 1:
                digits = [1, 0]
            else:
                digits[len(digits) - 2] += 1
                digits[len(digits) - 1] = 0
        else:
            digits[len(digits) - 1] += 1
        
        return digits