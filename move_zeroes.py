class Solution:
    def moveZeroes(self, nums):
        i = 0  # position to place the next non-zero element

        for j in range(len(nums)):
            if nums[j] != 0:
                # swap only when necessary
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
