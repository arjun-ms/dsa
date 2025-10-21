def isPalindrome(self, n):
    if n < 0:  # negative numbers are not palindromes
        return False
    rev = 0
    temp = n
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return temp == rev


# Alternate string based approach

def isPalindrome(self, n):
    s = str(n)
    return s == s[::-1]
