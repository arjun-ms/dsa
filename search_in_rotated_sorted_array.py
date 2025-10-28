class Solution:
    def search(self, nums, k):
        low = 0
        high = len(nums) - 1

        while low<=high:
            mid = (low+high)//2
            # mid = low + (high - low) // 2 (to prevent overflow errors in other languages)

            # check middle element
            if k == nums[mid]:
                return mid
                
            # Check if Left half is sorted
            if(nums[low]<=nums[mid]):
                # search in the left half,
                if nums[low] <= k and k <= nums[mid]:
                    high = mid - 1
                # else search in right half
                else:
                    low = mid + 1  

            # Check if Right half is sorted
            else:
                if nums[mid] <= k and k <= nums[high]:
                    low = mid + 1 # search in right half
                else:
                    high = mid - 1 # search in left half

        return -1 
