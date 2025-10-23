class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0  # handle empty input

        res = [nums[0]] # start with the first element

        for i in range(1,len(nums)):
            if nums[i] != res[-1]:
                res.append(nums[i])

        return len(res)

# This below code uses a set instead of list
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        set_ = set()
        for num in nums:
            set_.add(num)

        return len(set_)
      
# This uses extra space but we can do better with 2 ptrs

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0  # handle empty input

        j = 1  # next position to write a unique element
      
        # SKIP the first position
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1  # shift j whenever we find a unique element

        return j
