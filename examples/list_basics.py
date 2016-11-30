# Create empty list
empty_list = []
print(empty_list)

number_list = [2, 3, 4, 5, 6]
print(number_list)

# check see if python list can have mutiple data types
list_with_diff_types = [2, "Hello", 34.9, 'C']
print(list_with_diff_types)

# lists are oredered with index position 0...
print(number_list[0])

# slice a list to obtain a sub-list very similar to String slice
list_to_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# slice start index is inclusive and end index is exclusive
print(list_to_slice[2:6])

# add items to list by calling append
list_to_slice.append(100)
print(list_to_slice)

# Removing elements from list
list_of_numbers = [1, 2, 3, 4, 5]
print(list_of_numbers)
list_of_numbers.remove(2)
print(list_of_numbers)
del list_of_numbers[1]
print(list_of_numbers)
# You can also del + with slice
