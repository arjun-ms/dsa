class Solution:
    def isSorted(self, nums):
        i = 0
        j = 1

        while j<len(nums) and nums[j] >= nums[i]:
            i+=1
            j+=1

        return j == len(nums) # after loop, if j reached the end, array is sorted (True), otherwise not (False).
