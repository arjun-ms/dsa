class Solution:
    def divisors(self, n):
        op = []
        for i in range(1,n+1):
            if n%i==0:
                op.append(i)
        return op

# O(n) time complexity
# O(d) space (where d = number of divisors)

class Solution:
    def divisors(self, n):
        op = set()  # use a set to avoid duplicates
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                op.add(i)
                op.add(n // i) # If i divides n, then n // i is also a divisor.
        return sorted(op)
