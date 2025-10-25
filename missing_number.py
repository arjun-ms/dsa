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
