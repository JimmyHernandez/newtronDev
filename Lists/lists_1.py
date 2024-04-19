""" prompt the user to enter a number and, if the number is in the list,
remove its first occurrence. Show a message if deletion is not possible."""

list_sample = [1, 2, 5, 3, 4, 5, 6, 7, 8, 9]

print("List: ", list_sample)

while True:
    input_user = int(input("\nPlease enter a number to be eliminated from the list above (for exit type: 0): "))
    if input_user == 0:
        print("Bye bye")
        exit()
    else:
        list_sample.remove(input_user)
        print("The number selected is: ", input_user)
        print("The new list is : ", list_sample)

