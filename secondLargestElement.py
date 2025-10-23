class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)

        arr.sort()
        for i in range(n-2,-1,-1):
            # return the first element,
            # which is not equal to the 
            # largest element
            if arr[i]!=arr[n-1]:
                return arr[i]

        return -1
# T.C = O(nlogn)

# Optimal Solution below 

class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)

        largest = -1
        secondLargest = -1

        # check for greater than largest
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]

        # check for greater than secondLargest
        for j in range(n):
            if nums[j] > secondLargest and nums[j]!=largest:
                secondLargest = nums[j]

        return secondLargest

# T.C = O(n)
