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

# Use two pointer approach for this 
# Use approach to save the index of the first elements on both variables then check for 0 (value) after finding it save the index in first 
# and then use the second variable to store the index of non-zero element after that index of 0 stored in first element