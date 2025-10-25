class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
      
        temp = nums[0]
        
        for i in range(1,n):
            nums[i-1] = nums[i]

        
        nums[n-1] = temp

        return nums
