class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            n1, n2 = n2, n1 % n2  # simultaneous update
        
        return n1

# Time: O(log(min(n1, n2))) — extremely fast
# Space: O(1)
