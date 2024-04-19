""" Prompt the user to enter numbers, which will be saved in a list.
Finish by entering the number 0, which should not be saved."""

numbers = []

while True:

    input_numbers = int(input("Please enter a number. (for exit type: 0) :"))
    if input_numbers == 0:
        # numbers.append(input_numbers) <-- add this if you want to add the 0 to the list.
        break
    numbers.append(input_numbers)

print("The numbers you've entered to the list are: ", numbers)


