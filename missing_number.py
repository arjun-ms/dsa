class Solution:
    def missingNumber(self, nums):
        xor = 0

        for i in range(len(nums)+1):
            xor = xor ^ i 

        for num in nums:
            xor = xor ^ num

        return xor
