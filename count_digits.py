
def count_digits(n):
  cnt = 0
  
  while n>0:
    cnt = cnt + 1
    n = n//10 # remove the last digit.
    
  return cnt


#================ Another approach ==========================

# The count of digits can be calculated using log10(N) + 1.

import math
def count_digits_log(n):
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1
