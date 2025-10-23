class Solution:
    def twoSum(self, nums, target):
        hashmap = {} # {val_from_arr:idx}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[nums[i]] = i

        # Return an empty list if no solution is found
        return []
