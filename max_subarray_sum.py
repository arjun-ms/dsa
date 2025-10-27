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


# Kadane's Algo approach - O(n)

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

# Kadane's Algo approach - O(n)
class Solution:
    def maxSubArray(self, nums):  
        max_sum = nums[0]
        curr_sum = nums[0]
        n = len(nums)
        
        for i in range(1,n):
            # if current sum becomes negative, reset current sum
            if curr_sum<0:
                curr_sum = nums[i]
            else:
                curr_sum = curr_sum + nums[i]

            if curr_sum>max_sum:
                max_sum = curr_sum
            
        return max_sum


# Prefix Sum Method - O(n^2)
def max_subarray_sum_prefix(arr):
    n = len(arr)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            current_sum = prefix[j + 1] - prefix[i]
            max_sum = max(max_sum, current_sum)
    return max_sum
