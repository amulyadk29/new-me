# datatypes, var, operators
# r = float(input("enter the radius"))
# pi = 3.14
# a = pi * r * r
# print("area of circle:",a)

# str_1 = 'String enclosed in single quotes'
# print(str_1)
# str_2 = "String enclosed in double quotes"
# print(str_2)
# str_3 = '''String enclosed in triple quotes'''
# print(str_3)
# str_4 = 'String containing  " (double qoutes) enclosed in single quotes'
# print(str_4)
# str_5 = "String containing  ' (single qoute) enclosed in double quotes"
# print(str_5)
# str_6 = '''String containing both ' and " enclosed in triple quotes''' 
# print(str_6)
# multiple_lines = """Triple quotes also allow multi-line string."""
# print(multiple_lines)

# str_empty = ""
# print(str_empty)
# str_space = " "
# print(str_space) 
# str_single = "$"
# print(str_single)

# h = "hello"
# print(len(h))

# batman = "Bruce Wayne"
# first = batman[0]
# print(first)
# space = batman[6]
# print(space)
# last = len(batman)
# print(last)

# string = u"This is unicode"
# u = None
# print(type(u))

# list = [1,2.3,True,"hello"]
# print(list)
# print(len(list))
# print(list[3])
# list[3]="hiii"
# print(list)
# print(len(list))
# list = ["hello","how are you","bye"]
# print(list[1][2])
# print(list[2][1])
# list=["hello"]
# list[0]="jello"
# print(type(list))
# print(list)

# name_list = ["John", "Doe", "Smith"]  # List containing first, middle, and last names

# first_initial = name_list[0][0]# Extract the first initial
# middle_initial = name_list[1][0]# Extract the middle initial
# last_initial =   name_list[2][0]# Extract the last initial
# initials_list =  [first_initial, middle_initial, last_initial]# Create a new list to store the initials
# print(initials_list)          # Display the initials list

# var_1 = var_2 = var_3 = 10
# print(var_1)
# print(var_2)
# print(var_3)

# var_2 = 15
# print(var_1)
# print(var_2)
# print(var_3)

# add
# print(0+7)
# print(3.5+3)
# print(4.2+7.7)
# sub
# print(3-3)
# print(5.5-8)
# print(9.1-10.5)
# mul
# print(1*2)
# print(3.4*5.6)
# print(7*8.9)
# div
# print(9/3.6)
# print(6/7)
# floor div
# print(7.2//4.5)
# print(8.9//5)
# modulus
# print(10%3)
# print(-29 % 10)  # The remainder is positive if the right-hand operand is positive
# print(28 % -10)  # The remainder is negative if the right-hand operand is negative
# print(34.4 % 2.5)
# exponent 
# print(2**2)#4
# print(1.4**1.5)
# print(13**1.6)

# Different precedence
# print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction
# Same precedence
# print(3 * 20 / 5)  # Multiplication computed first, followed by division
# print(3 / 20 * 5)  # Division computed first, followed by multiplication

# print((10 - 3) * 2) 
# print((18 + 2) / (10 % 8))

# num = 10
# num += 5    # num=num+5
# print(num)  
# num -= 3    # num=num-3
# print(num)  
# num *= 2    # num=num*2
# print(num)  
# num /= 2    # num=num/2
# print(num)  
# num //= 3   # num=num//3
# print(num)  
# num %= 3    # num=num%3
# print(num) 
# num **= 2   # num=num**2
# print(num) 

# The result of a comparison is always a bool.
# num = 10
# nim = 20
# nam = 30
# print(num < nim)  #true
# print(nam > nim)  #t
# print(num==nim)   #f
# print(nam!=num)   #t
# print(3+4==6-5)     f
# print(6>=8)         f

# original_list = [1, 2, 3]
# same_reference_list = original_list
# different_list = [1, 2, 3]
# reordered_list = [1, 3, 2]

# print(original_list is same_reference_list) #true
# print(original_list is different_list)      #false
# print(original_list == different_list)      #true
# print(original_list == reordered_list)      #false

# first_number = 10
# second_number = 20
# third_number = 10
# print(first_number is not second_number)  #true
# print(first_number is not 10)           #false

# same_reference_number = first_number    true
# print(same_reference_number is first_number) 

# first_number = 0.1 + 0.2  
# second_number = 0.3
# print(first_number == second_number)
# print(f"first_number: {first_number:.20f}")
# print(f"second_number: {second_number:.20f}")

# print(10 + True)
# print(10 + False)
# print (True + False)

# print('a' < 'b')  # 'a' has a smaller Unicode value a=65, b=66 true

# house = "Gryffindor"
# house_copy = "Gryffindor"

# print(house == house_copy)

# new_house = "Gwyffindor"

# print(house == new_house)

# print(new_house <= house)

# print(new_house >= house)

# one = "hello"
# two = "world"
# new = one + two #string Connection 
# print(new)

# one = "hello"
# two = 34
# # new = one + two # error cuse its strig concat not with int
# new = one + str(two) #covert int to string
# print(new)
# print("hello"*3)

# random_string = "This is a random string"

# print('of' in random_string)  # Check whether 'of' exists in randomString
# print('random' in random_string)  # Check whether 'random' exists!
# print('hello' not in random_string)  # Check whether 'hello' does not exist in random_string

# i = "this is me and am done for the day"
# print(i[0:3])
# print(i[::])    #full string
# print(i[:])      #full string
# print(i[::2])    
# print(i[8:len(i)])
# print(i[0:3:4])
# print(i[-1:-5:-1])
#string[start:end:step]

# my_string = "This is MY string!"
# print(my_string[:8])   # All the characters before 'M'
# print(my_string[8:])   # All the characters starting from 'M'
# print(my_string[:])    # The whole string
# print(my_string[::-1]) # The whole string in reverse (step is -1)

# filename = "data_2022_01_15.csv"

# index = filename.index("_")
# print(filename[index+1:index+11])

# Basic variable insertion
# name = "ABC"
# age = 30
# print(f"My name is {name} and I am {age} years old")

#  Arithmetic operations
# a = 10
# b = 20
# print(f"The sum of {a} and {b} is {a + b}")

# Specifying decimal precision
# pi = 3.14159265359
# print(f"The value of pi is {pi:.2f}")
# print(f"The value of pi is {pi:.5f}")

#  Padding with zeros
# number1 = 5
# number2 = 79
# print(f"Number after padding {number1:03}")
# print(f"Number after padding {number2:03}")

# stud = 20
# if stud >= 35:
#     print("pass")
# else:
#     print("give exam again")

# i = 10
# if i == 0:
#     print("num is = 0")

#     if i > 1:
#         print("num s greater than 1")

# num = 12
# if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
     # Only works when num is a multiple of 2, 3, and 4
#     print("The number is a multiple of 2, 3, and 4")

# if (num % 5 == 0 or num % 6 == 0):
     # Only works when num is either a multiple of 5 or 6
#     print("The number is a multiple of 5 or 6")

# n = 76
# if  n>=10 and n<80:
#     if n>50 and n<79:
#      if n>74 and n<77:
#         print("num is b/w 74 to 77")

# n = 15
# if n>10:
#     n = 25
#     i = n*2
#     print(i)
#     print(n)

# numerator = 10
# denominator = 20
# if denominator != 0 and numerator % denominator == 0:
#         print("remainder is zero")
#     print("denominator is zero")

# age = input("enter ur age")
# if (age >= 18 and age <= 70) and
# (annual_income >= 50000 or monthly_income >= 3000) and(has_default == false):

# n = 60
# if n>30:
#     print("true")
# if n<=45:
#     print("false")

#ternory operator
# n = 60
# o = "the num is less than or equal to 50" \
# if n <= 50 else "the num is greater than 50"
# print(o)

# light = "Red"
# if light == "Green":
#     print("Go")

# elif light == "Yellow":
#     print("Caution")

# elif light == "Red":
#     print("Stop")

# else:
#     print("Incorrect light signal")

# num = 5

# if num == 0:
#     print("Zero")
# elif num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# elif num == 4:
#     print("Four")
# elif num == 5:
#     print("Five")
# elif num == 6:
#     print("Six")
# elif num == 7:
#     print("Seven")
# elif num == 8:
#     print("Eight")
# elif num == 9:
#     print("Nine")

# num = 10

# if num > 5:
#     print("The number is greater than 5")
# if num % 2 == 0:
#     print("The number is even")
# if not num % 2 == 0:
#     print("The number is odd")

# AQI = 75

# if AQI >= 0 and AQI <= 50:
#   print("Green")
# elif AQI > 50 and AQI <= 100:
#   print("Yellow")
# elif AQI > 100 and AQI <= 150:
#   print("Orange")
# elif AQI > 150 and AQI <= 200:
#   print("Red")
# elif AQI > 200 and AQI <= 300:
#   print("Purple")
# elif AQI > 300 and AQI <= 500:
#   print("Maroon")
# else:
#   print("Incorrect Value")

#You might expect this to return True, but due to the way floating=point arithmetic works, 
# it returns False. The result of 0.1 + 0.2 is actually 0.30000000000000004, not exactly 0.3.
# print (0.1 + 0.2 == 0.3) 

# import math

# a = 0.1 + 0.2
# b = 0.3
# print(math.isclose(a, b)) 
# import math

# a = 0.1 + 0.2
# b = 0.3

# print(math.isclose(a, b, rel_tol=1e-9)) 
# print(math.isclose(a, b, rel_tol=1e-20))  

# import math

# a = 0.1 + 0.2
# b = 0.3

# print(math.isclose(a, b, rel_tol=1e-9))
# print(math.isclose(a, b,  abs_tol=1e-12))

# score = 85
# if score>=90 and score<=100:
#     print("a")
# elif score>=80 and score<=89:
#     print("b")
# elif score>=70 and score<=79:
#     print("c")
# elif score>=60 and score<=69:
#     print("d")
# else:
#     print("f")

# price = 250
# if price >= 300:
#     price *= 0.7  # (1 - 0.3)
# elif price >= 200:
#     price *= 0.8  # (1 - 0.2)
# elif price >= 100:
#     price *= 0.9  # (1 - 0.1)
# elif price < 100 and price >= 0:
#     price *= 0.95  # (1 - 0.05)

# print(price)
   
# string fomating
# Basic variable insertion
# name = "ABC"
# age = 30
# print(f"My name is {name} and I am {age} years old")

# Arithmetic operations
# a = 10
# b = 20
# print(f"The sum of {a} and {b} is {a + b}")

# Specifying decimal precision
# pi = 3.14159265359
# print(f"The value of pi is {pi:.2f}")
# print(f"The value of pi is {pi:.5f}")

# Padding with zeros
# number1 = 5
# number2 = 79
# print(f"Number after padding {number1:03}")
# print(f"Number after padding {number2:03}")

# before this we  using %
# string1 = "I like %s" % "Python"
# print(string1) 

# temp = "Educative"
# string2 = "I like %s" % temp
# print(string2) 

# string3 = "I like %s and %s" % ("Python", temp)
# print(string3)  

# diff fomat exaples
# name = "Alice"
# age = 30
# pi = 3.14159
# scientific = 0.000123
# hex_value = 255

# print("Name: %s" % name)
# print("Age: %d" % age)
# print("Pi: %.2f" % pi)
# print("Scientific: %.2e" % scientific)
# print("Hex: %x" % hex_value)

# string1 = "%f" % (2)
# print(string1)

# string2 = "%.2i" % (1.11)
# print(string2)

# float2 = "%.2f" % (1.117)
# print(float2)

# float1 = "%.5f" % (3.14159265359)
# print(float1)