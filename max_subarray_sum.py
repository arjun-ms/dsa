class Solution:
    def maxSubArray(self, nums):
    
        max_sum = float('-inf')
        n = len(nums)
        
        for i in range(n):
            curr_sum = 0
            for j in range(n):
                curr_sum += nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
        
        return max_sum


# Kadane's Algo approach

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            # reset the current Sum to 0 whenever you get a negative result 
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum,currSum)
        return maxSum
