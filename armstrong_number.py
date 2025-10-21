class Solution:
    def isArmstrong(self, n):
        sum_of_cubes = 0
        num = n

        while n!=0:
            digit = n%10
            sum_of_cubes += digit*digit*digit
            n = n//10

        return sum_of_cubes==num 


# Generalized armstrong checker

class Solution:
    def isArmstrong(self, n):
        num = n
        digits = len(str(n))  # number of digits
        total = 0

        while n != 0:
            digit = n % 10
            total += digit ** digits
            n = n // 10

        return total == num

