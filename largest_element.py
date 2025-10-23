class Solution:
    def largestElement(self, nums):
        maxi = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
        
        return maxi
