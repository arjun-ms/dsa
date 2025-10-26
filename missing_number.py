class Solution:
    def missingNumber(self, nums):
        xor = 0

        # XOR all numbers from 0 to n
        for i in range(len(nums)+1):
            xor = xor ^ i 

        # XOR all numbers in the array
        for num in nums:
            xor = xor ^ num

        return xor

# a ^ a = 0 
# a ^ 0 = a
# a ^ b ^ c = c ^ a ^ b (commutative and assosiative)

"""
(0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)
= (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2
= 0 ^ 0 ^ 0 ^ 2
= 2
"""

# Brute Force
# Time Complexity : O(n^2)
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        for i in range(n + 1):  # check numbers from 0 to n
            found = False
            for j in range(n):  # search for i in array
                if nums[j] == i:
                    found = True
                    break
            if not found:
                return i


# Hashing Method
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        num_set = set(nums)   # store all elements for O(1) lookups
        
        for i in range(n + 1):  # check all numbers from 0 to n
            if i not in num_set:
                return i
