"""Generate and print a new list that contains tuples of two elements as elements, each composed of a number from
the original list and the number of times it appears in it. For example, if the original list is [5,16,2,5,57,5,2]
the new list will contain: [(5,3), (16,1), (2,2), (57, 1)]"""


def repetitions(lista_original, numbers):
    count = 0
    for num in lista_original:
        if num == numbers:
            count += 1
    return count


sample_list = [5, 16, 2, 5, 57, 5, 2]
new_list = []

for number in sample_list:
    occurrences = repetitions(sample_list, number)
    new_tuple = (number, occurrences)
    new_list.append(new_tuple)

clean_list = set(new_list)
new_list2 = [clean_list]
print(new_list)
print(new_list2)
