# Create empty list
empty_list = []
print(empty_list)

number_list = [2, 3, 4, 5, 6]
print(number_list)

# check see if python list can have multiple data types
list_with_diff_types = [2, "Hello", 34.9, 'C']
print(list_with_diff_types)

# lists are ordered with index position 0...
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
print("Removing 2 from list")
list_of_numbers.remove(2)
print(list_of_numbers)
print("Removing element with index position 1 from list")
del list_of_numbers[1]
print(list_of_numbers)
# You can also del + with slice

# Dictionaries - similar to a list but more rather a set, the ':' assigns the key BA to British Airways
plane_acronyms = {'BA': 'British Airways', 'UL': 'Sri Lankan Airlines', 'EK': 'Emirates'}
print(plane_acronyms['UL'])
print(plane_acronyms['EK'])
print(plane_acronyms)
# Adding a new value to dictionary
plane_acronyms['SQ'] = 'Singapore Airlines'
print(plane_acronyms)
# Removing a value from dict using key
del plane_acronyms['EK']
print(plane_acronyms)
# Checking to see if a value exist
plane_ack_exist = plane_acronyms.get('UL')
print("UL exists", plane_ack_exist)
# Query for key that does not exist - will return NONE (special python value - absence of a value)
# None also evaluates to False in a conditional statement
unknown_plane_ack = plane_acronyms.get('UNKNOWN')
print(unknown_plane_ack)


# Comparing equality with lists, have to be same items and same order
list_one = [1, 2, 3, 4, 5]
list_two = [1, 2, 3, 4, 5]
list_three = [1, 3, 2, 4, 5]
print(list_one == list_two)
print(list_one == list_three)
# Comparing dict only need to have same value
dict_one = {1: 1, 2: 2, 3: 3}
dict_two = {2: 2, 1: 1, 3: 3}
print(dict_one == dict_two)

# Example of two dimensional array
parent_list = [["747", "787", "737", "777"],
               ["A320", "A330", "A340", "A380"],
               ["MD-11", "DC1030", "LR1101-TriStar"]]
print(parent_list)

# Example of having a two dimensional array in a dict
air_craft_dic = {"Boeing": ["747", "787", "737", "777"],
                 "Airbus": ["A320", "A330", "A340", "A380"],
                 "McDonnell Douglas": ["MD-11", "DC1030", "LR1101-TriStar"]}
print("Aircraft dictionary", air_craft_dic)

# Example of two dimensional dic
multi_dim_dic = {"Boeing": {"747": "Mega Top", "777": "My Favourite"},
                 "Airbus": {"A380": "Double Decker", "A320": "Twin Engine short haul", "A350": "Next Gen med-long haul"}
                 }
# printing certain elements from multi dimensional dic, e.g. print value of key 777
print("Print value of \"Boeing\" and \"777\" is =", multi_dim_dic["Boeing"]["777"])
print("Get value of A320 from Airbus dic", multi_dim_dic.get("Airbus").get("A320"))
print("Prints python special value NONE for querying key that does not exist", multi_dim_dic.get("Airbus").get("A333"))

