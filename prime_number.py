# Definition : A number that has exactly 2 factors: 1 and itself

# T.C = O(n)

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
        
        return cnt == 2

# =================== Efficient way below ======================================

# T.C = O(√n)
class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
