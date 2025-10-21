# Optimized way to print divisors

num = int(input("Enter a number: "))

divisors = set()
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        divisors.add(i)
        # if i != num//i: # since we are appending to a set this is not required
        divisors.add(num // i)

print(f"Divisors of {num} are: {sorted(divisors)}")
