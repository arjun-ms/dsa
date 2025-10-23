class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n-1): # say n=6 ;  i will go from 0 to 4(included)
            mini = i
            for j in range(i+1,n):
                if nums[j] < nums[mini]:
                    mini = j

            temp = nums[mini]
            nums[mini] = nums[i]
            nums[i] = temp
        return nums 

# Time Complexity = O(n^2)
# Auxiliary Space = O(1).
