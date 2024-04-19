"""Prompt the user for another number and create a list with the items in the original
list that are less than the given number. Print this new list, iterating through it."""

numbers = [1, 2, 3, 5, 15, 27]

input_numbers = int(input("Please enter a number. (for exit type: 0) :"))

new_list = []
for num in numbers:
    if num < input_numbers:
        new_list.append(num)

print("The old list is: ", numbers)
print("The new list is: ", new_list)
