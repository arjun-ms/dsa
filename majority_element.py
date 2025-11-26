# 1. Sorting Approach (O(n log n) time, O(1) space)
class Solution:
    def majorityElement(self, nums):
        nums.sort()                     # O(n log n)
        return nums[len(nums) // 2]     # middle element is always the majority

# 2. Hash Map / Frequency Count (O(n) time, O(n) space)
class Solution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        half = len(nums) // 2

        for num, count in freq.items():
            if count > half:
                return num

# 3. Boyer–Moore Majority Vote (O(n) time, O(1) space)
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:          # choose new candidate
                candidate = num

            if num == candidate:    # same → increase confidence
                count += 1
            else:                   # different → decrease confidence
                count -= 1

        return candidate
