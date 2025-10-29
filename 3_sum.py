class Solution:
    def threeSum(self, nums):
        # [-1,0,1,2,-1,-4]
        #   i j         k

        res = [] # to store the triplets

        # sort the i/p array
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate elements
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i]+nums[j]+nums[k] 
                if total < 0:
                    # increment j
                    j = j+1
                elif total > 0:
                    # decrement k
                    k = k-1
                else: # if total equals 0
                    res.append([nums[i],nums[j],nums[k]])
                    j = j+1

                    # increment j ptr to skip duplicate elements
                    while nums[j] == nums[j-1] and j < k:
                            j += 1
            
        return res
