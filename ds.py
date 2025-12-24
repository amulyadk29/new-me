# n = ["hello"]
# print(n.copy())
# n = [1,2,3]  #or "hello"
# i = 0
# while i < len(n):
#     print(n[i])
#     i+=1

# in built for list data structre
# n_seq = range(0, 10)  # A sequence from 0 to 9
# n_list = list(n_seq)  # The list() method casts the sequence into a list
# print(n_list)

# n_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
# print(list(n_seq))

# world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
#                      [2014, "Germany"], [2018, "France"]]
# print(world_cup_winners)

# list = ["Jon Snow", "Winterfell", 30]
# print(list)

# part_A = [1, 2, 3, 4, 5]
# part_B = [6, 7, 8, 9, 10]
# merged_list = part_A + part_B         2.  #part_A.extend(part_B)
                                            #print(part_A)
# print(merged_list)

# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i = j = 0
    
#     # Merge the two lists
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])                # Append remaining elements (if any)
#             j += 1
    
#     merged_list.extend(list1[i:])
#     merged_list.extend(list2[j:])
    
#     return merged_list

# num_list = []  # Empty list
# num_list.append(1)
# num_list.append(2)
# num_list.append(3)
# print(num_list)

# num_list = [1, 2, 3, 5, 6]
# num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
# print(num_list)

# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# last_house = houses.pop()
# print(last_house)
# print(houses)

# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# print(houses)
# houses.remove("Ravenclaw")
# print(houses)

# # For nested lists
# populations = [["Winterfell", 10000], ["King's Landing", 50000],
#                ["Iron Islands", 5000]]
# print(populations)
# populations.remove(["King's Landing", 50000])
# print(populations)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(num_list[2:5])
# print(num_list[0::2])

# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print(cities.index("Los Angeles"))  # It is at the index 2

# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print("London" in cities)
# print("Moscow" not in cities)

# num_list = [20, 40, 10, 50.4, 30, 100, 5]
# num_list.sort()
# print(num_list)

# nums = [10, 20, 30, 40, 50]
# nums_double = []

# for n in nums:
#     nums_double.append(n * 2)

# print(nums)
# print(nums_double)

# nums = [10, 20, 30, 40, 50]

# # List comprehension
# nums_double = [n * 2 for n in nums if n%4==0]

# print(nums)
# print(nums_double) 

# list1 = [30, 50, 110, 40, 15, 75]
# list2 = [10, 60, 20, 50]
# sum_list = [[n1, n2] for n1 in list1 for n2 in list2 if n1 + n2 > 100]
# print(sum_list)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = [i for i in nums if nums%2==0]
# print(res)

# tuple

# car = ("Ford", "Raptor", 2019, "Red")
# print(car)
# # Length
# print(len(car))
# # Indexing
# print(car[1])
# # Slicing
# print(car[2:])

# hero_names = ("Batman", "Wonder Woman", "Superman")
# hero_ages = (35, 80, 40)
# hero_powers = ("Martial Arts", "Super Strength", "Flight")
# merged_heroes_info = hero_names + hero_ages + hero_powers
# print(merged_heroes_info)

# hero1 = ("Batman", "Bruce Wayne", 35, 85.5)
# hero2 = ("Wonder Woman", "Diana Prince", 80, 99.9)
# awesome_team = (hero1, hero2)
# print(awesome_team)

# cities = ("London", "Paris", "Los Angeles", "Tokyo")
# print("Tokyo" in cities)
# print("Moscow" in cities)

# cities_set1 = ("London", "Paris", "Los Angeles", "Tokyo")
# print(cities_set1.index("Tokyo"))

# cities_set2 = (
#     ("London", 8.9, "UK"),
#     ("Paris", 2.1, "France"),
#     ("Los Angeles", 3.9, "USA"),
#     ("Tokyo", 14.0, "Japan")
# )

# tokyo_index = [city[0] for city in cities_set2].index("Tokyo")
# print(f"Index of Tokyo: {tokyo_index}")

#dictionary

# empty_dict = {} 
# print(empty_dict)

# phone_book = {
#     'Alice': 1234567890,
#     'Bob': 9876543210,
#     'Charlie': 'unknown',
#     123: 5555555.55
# }
# print(phone_book)

# empty_dict = dict()  # Empty dictionary
# print(empty_dict)

# phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
# print(phone_book)

# Alternative approach
# phone_book = dict([('Batman', 468426),
#                    ('Cersei', 237734),
#                    ('Ghostbusters', 44678)])
# print(phone_book)

# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book["Cersei"])
# print(phone_book.get("Ghostbusters"))

# add
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)

# phone_book["Godzilla"] = 46394  
# print(phone_book)

# phone_book["Godzilla"] = 9000  
# print(phone_book)

# remove
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)

# del phone_book["Batman"]
# print(phone_book)

# pop() & popitem()
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)

# cersei = phone_book.pop("Cersei")
# print(phone_book)
# print(cersei)

# lastAdded = phone_book.popitem()
# print(lastAdded)

# len
# phone_book = {"Batman": 468426,
            #   "Cersei": 237734,
            #   "Ghostbusters": 44678}
# print(len(phone_book))

# key excistance using in
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print("Batman" in phone_book)
# print("Godzilla" in phone_book)

# update
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}

# second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
# phone_book.update(second_phone_book)
# print(phone_book)

# def update_phone_book(phone_book, new_entries):
#   phone_book.update(new_entries)


# phone_book = {"Spiderman": 123456, "Hulk": 654321}
# new_entries = {"Thor": 789123, "Hulk": 111111}
# update_phone_book(phone_book, new_entries)
# print(phone_book)  

# Dictionary comprehension
# houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
# new_houses = {n*2: house + "!" for (n, house) in houses.items()}
# print(houses)
# print(new_houses)

# squares = {1: 1, 2: 4, 3: 9, 4: 16}
# new_squares = {key*2: value+1 for key, value in squares.items()}
# print(new_squares) 

# quiz
# my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]

# my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
# print(my_tuple)

# test_list = [40, 35, 82, 14, 22, 66, 53]
# k = 2

# test_list.sort()
# kth_max = test_list[-k]
# print(kth_max)

# set()

# random_set = {"Educative", 1408, 3.142,
#               (True, False)}
# print(random_set)
# print(len(random_set))  # Length of the set
# random_set.add(5555)
# print(random_set) 

# how to create different data structures in Python
# test_set = {"Educative", 1408, 3.142, (True, False)}
# test_lst = ["Educative", 1408, 3.142, (True, False)]
# test_dic = {1: "Educative", 2: 1408, 3: 3.142, 4: (True, False)}
# test_tup = ("Educative", 1408, 3.142, (True, False))

# print(type(test_set))  
# print(type(test_lst))  
# print(type(test_dic))  
# print(type(test_tup))  

#adding elements
# empty_set = set()
# print(empty_set)

# empty_set.add(1)
# print(empty_set)

# empty_set.update([2, 2, 3, 4, 5, 5, 5, 6])
# print(empty_set)

# Set comprehension
# squares_set = {x**2 for x in range(10)}
# print(squares_set)
# even_set = {x for x in range(1, 11) if x % 2 == 0}
# print(even_set)

# itiratin set using for loop
# odd_list = [1, 3, 5, 7]
# unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

# print(unordered_set)

# for n in unordered_set:
#     if(not n % 2 == 0):
#         odd_list.append(n)

# print(odd_list)

# union set

# set_A = {1, 2, 3, 4}
# set_B = {'a', 'b', 'c', 'd'}
# print(set_A | set_B)
# print(set_A.union(set_B))
# print(set_B.union(set_A))
# Define two sets
# itersection
# set_A = {1, 2, 3, 4}
# set_B = {2, 8, 4, 16}
# print(set_A & set_B)
# print(set_A.intersection(set_B))
# print(set_B.intersection(set_A))
# Difference 
# print(set_A - set_B)
# print(set_A.difference(set_B))
# print(set_B - set_A)
# print(set_B.difference(set_A))
# Symmetric difference
# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}
# sym_diff_method = set_A.symmetric_difference(set_B)
# print("Symmetric difference using symmetric_difference() method:", sym_diff_method)
# sym_diff_reverse_operator = set_B ^ set_A
# print("Symmetric difference using set_B ^ set_A:", sym_diff_reverse_operator)

# ds convertions------explicit covertion>>>>>>list convrtion

# Tuple of Star Wars characters and a number
# star_wars_tup = ("Anakin", "Darth Vader", 1000)
# print(star_wars_tup)

# # Set of Star Wars characters and a number
# star_wars_set = {"Anakin", "Darth Vader", 1000}
# print(star_wars_set)

# # Dictionary mapping numbers to Star Wars characters
# star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
# print(star_wars_dict)

# # Converting the tuple to a list
# star_wars_list_from_tup = list(star_wars_tup)
# print(star_wars_list_from_tup)

# # Converting the set to a list
# star_wars_list_from_set = list(star_wars_set)
# print(star_wars_list_from_set)

# # Converting the keys of the dictionary to a list
# star_wars_list_from_keys = list(star_wars_dict.keys())
# print(star_wars_list_from_keys)

# # Converting the values of the dictionary to a list
# star_wars_list_from_values = list(star_wars_dict.values())
# print(star_wars_list_from_values)

# # Converting the items (key-value pairs) of the dictionary to a list
# star_wars_list_from_items = list(star_wars_dict.items())
# print(star_wars_list_from_items)

# star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
# print(star_wars_dict)

# star_wars_list = list(star_wars_dict.items())
# print(star_wars_list)

# Converting to a tuple
# List of Star Wars characters and a number
# star_wars_list = ["Anakin", "Darth Vader", 1000]
# print(star_wars_list)

# # Tuple of Star Wars characters and a number
# star_wars_tup = ("Anakin", "Darth Vader", 1000)
# print(star_wars_tup)

# # Dictionary mapping numbers to Star Wars characters
# star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
# print(star_wars_dict)

# # Converting the list to a tuple
# star_wars_tuple_from_list = tuple(star_wars_list)
# print(star_wars_tuple_from_list)

# # Converting the tuple to a new tuple (redundant but for demonstration)
# star_wars_tuple_from_tup = tuple(star_wars_tup)
# print(star_wars_tuple_from_tup)

# # Converting the keys of the dictionary to a tuple
# star_wars_tuple_from_keys = tuple(star_wars_dict.keys())
# print(star_wars_tuple_from_keys)

# # Converting the values of the dictionary to a tuple
# star_wars_tuple_from_values = tuple(star_wars_dict.values())
# print(star_wars_tuple_from_values)

# # Converting the items (key-value pairs) of the dictionary to a tuple
# star_wars_tuple_from_items = tuple(star_wars_dict.items())
# print(star_wars_tuple_from_items)


# set
# # List of Star Wars characters and a number
# star_wars_list = ["Anakin", "Darth Vader", 1000]
# print(star_wars_list)

# # Tuple of Star Wars characters and a number
# star_wars_tup = ("Anakin", "Darth Vader", 1000)
# print(star_wars_tup)

# # Dictionary mapping numbers to Star Wars characters
# star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
# print(star_wars_dict)

# # Converting the list to a set 
# star_wars_set_from_list = set(star_wars_list)  
# print(star_wars_set_from_list)

# # Converting the tuple to a set 
# star_wars_set_from_tup = set(star_wars_tup)  
# print(star_wars_set_from_tup)

# # Converting the keys of the dictionary to a set 
# star_wars_set_from_dict = set(star_wars_dict)  
# print(star_wars_set_from_dict)

# # Converting the keys of the dictionary to a set
# star_wars_set_from_dict = set(star_wars_dict.keys())
# print(star_wars_set_from_dict)

# # Converting the values of the dictionary to a set
# star_wars_set_from_dict = set(star_wars_dict.values())
# print(star_wars_set_from_dict)

# # Converting the items of the dictionary to a set
# star_wars_set_from_dict = set(star_wars_dict.items())
# print(star_wars_set_from_dict)

# Converting to a dictionary
# List of Star Wars characters with their corresponding IDs
# star_wars_list = [[1, "Anakin"], [2, "Darth Vader"], [3, 1000]]
# print(star_wars_list)

# # Tuple of Star Wars characters with their corresponding IDs
# star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
# print(star_wars_tup)

# # Set of Star Wars characters with their corresponding IDs
# star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
# print(star_wars_set)

# # Converting the list of pairs to a dictionary
# star_wars_dict_from_list = dict(star_wars_list)  
# print(star_wars_dict_from_list)

# # Converting the tuple of pairs to a dictionary
# star_wars_dict_from_tup = dict(star_wars_tup)  
# print(star_wars_dict_from_tup)

# # Converting the set of pairs to a dictionary
# star_wars_dict_from_set = dict(star_wars_set) 
# print(star_wars_dict_from_set)

# quiz 3 ___-------Solution 1: Using filter and lambda

# def count_low_high(num_list):
#     if (len(num_list)==0):
#         return None
#     high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
#     low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
#     return [len(low_list), len(high_list)]

# num_list = [20, 9, 51, 81, 50, 42, 77]
# print(count_low_high(num_list))

# Solution 2: List comprehension

# def count_low_high(num_list):
#     if (len(num_list)==0):
#         return None
#     high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
#     low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
#     return [low_list, high_list]

# num_list = [20, 9, 51, 81, 50, 42, 77]
# print(count_low_high(num_list))