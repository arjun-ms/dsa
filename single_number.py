# time complexity = O(n²)
# space complexity = O(n)
class Solution:
    def singleNumber(self, nums):
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1

            if count == 1:
                return nums[i]

# time = O(n)
class Solution:
    def singleNumber(self, nums):
        freq = {}

        # Step 1: Count frequency of each number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Find the number that appeared once
        for num in freq:
            if freq[num] == 1:
                return num

# XOR all elements in array
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num   # XOR all numbers
        return result

  # Step-by-step XOR:
# (1 ^ 2 ^ 2 ^ 4 ^ 3 ^ 1 ^ 4) → all pairs cancel → 3
