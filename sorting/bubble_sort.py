class Solution:
    def bubbleSort(self, nums):

        n = len(nums)
        for i in range(n):
            for j in range(n-i-1): # Each pass “bubbles up” the largest unsorted element to the end, so the next pass doesn’t need to touch those sorted tail elements again.
                if nums[j] > nums[j+1]:
                    # swap
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
            
        return nums
