# Ask the user to enter a number repeatedly.
# If the input is invalid, ask again.
# When a valid integer is entered, print its square and stop the program.


## Retries on invalid input WITHOUT showing any error message (silent retry)

while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        pass
    else: 
        square = num * num
        print(f"Square is: {square}")
        break

###   else → runs only when no error occurs   ###

## Retries on invalid input WITH an error message shown to the user

while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Enter a valid number")
    else:
        square = num * num
        print(f"Square is: {square}")
        break   # exit the loop after valid input
