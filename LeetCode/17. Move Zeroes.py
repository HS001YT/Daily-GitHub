# First Approch is simple it takes the non - zeroes number in the begining and then set the remaining sapaces of the list with zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        
        # Fill remaining positions with 0
        for i in range(pos, len(nums)):
            nums[i] = 0

# Second Approch includes two pointers which helps to swap as well as maintain the data in original order

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lptr = 0
        for rptr in range(len(nums)):
            if nums[rptr]:          # Works for non zero as in boolean 0 is false and everything else is true
                nums[lptr], nums[rptr] = nums[rptr], nums[lptr]
                lptr += 1