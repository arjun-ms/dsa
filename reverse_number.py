def reverseNumber(self, n):
    rev_str = ""
    while n!=0:
        last = n%10 # extraction of last digit
        rev_str += str(last)
        n = n//10 # removal of last digit

    return rev_str

# T.C = O(d^2)  ; (where d is the number of digits in the number)
# S.C = O(d)    ; 

# This is not optimal 

# String concatenation inside a loop (rev_str += str(last))
# This creates a new string each time since Python strings are immutable.

# Time complexity: roughly O(d²) for a number with d digits.
# Doesn’t handle negative numbers
# For example, -123 will cause an infinite loop.

# Returns a string, not an integer
# Typically, reversing a number means returning a number, not a string.


# Optimal Way

# Time Complexity       O(d) ;   Each iteration does constant work, no redundant copying.
# Space Complexity      O(1) ;   only uses a few variables (rev, n, sign).

def reverseNumber(self, n):
        if n<0:
            sign = -1
        else:
            sign = 1

        n = abs(n)
        rev = 0
        while n!=0:
            digit = n%10 # digit extraction
            rev = rev * 10 + digit # add extracted digit to the number
            n = n//10  # remove last digit

        return sign*rev

