# 3. Build Your Own Commands
# build in and user defined functions

# def greet():
#     print("hello world")
    
# greet()

# def greet(name):
#     print("hello",name)

# greet("alex")   
# greet("sam") 

# def add(a,b):
#     return a+b
# res = add(3,4)
# print(res)

# def favorite_movie(movie):
#     print("my fav movie is",movie)

# favorite_movie("zoo") 

# def fun_story():
#     print("you stand at the fork in te road")
#     choice = input("left or right?") 

#     if choice == "left":
#      print("you are in middle of jungle")
#     elif choice == "right":
#      print("you are at beatch")
#     else:
#      print("u missed the point")   

# fun_story()   
 
# def fun_story():
#      print("you stand at the fork in te road")
#      choice = input("left or right?")
#      if choice == "left":
#           print("you are in middle of jungle")
#           next_choice =input("u want to move forward or backward?")
#           if next_choice == "forward":
#                print("you see a elephant")  
#           elif next_choice == "backward":
#                print("u are in starting point")
#           else:
#                print("this is not b or f")
#      elif choice == "right":
#       print("u r at beatch")
#       next_choice =input("u want to play or go back to room?")
#       if next_choice == "play":
#           print("it will be more fun")
#       elif next_choice == "go back to room":
#           print("u r in room")
#       else:
#           print("no a validone")

#      else:
#           print("u have to choice any 1 of the above")
# fun_story()

# dict
# person ={
#      "name":"alexa",
#      "age":21,
#      "city":"london"
#  }
# for key ,value in person.items():
#     print(key ,value)

#  person ={
#      "name":"alexa",
#      "age":21,
#      "city":"london"
#  }
#  print(person["age"])
#  person["age"]=22
#  person["name"]="nick"
#  print(person)

# Write your code here.
# me ={
#     "name":"sam",
#     "hobby":"drawing",
#     "language":"kannada",
#     "fav_color":"green",
#     "game":"cricket"
# }
# for key,value in me.items():
#   print(key, ":" ,value)

# Write your code here.
# contact = {
#     "fam":2342324,
#     "frnd":342678,
#     "places":"mumbai"
# }
# print("pick my call lets go for trip",contact["frnd"] )

# list and dict
# people =[
#     { "name":"alex", "age":23},
#     { "name":"ira", "age":27},
#     { "name":"intel", "age":26}
# ]
# for am in people:
#     print("i am",am["name"],"and am",am["age"],"years old")

# Write your code here.
# school =[
#     {"name":"max","score":76},
#     {"name":"devil","score":93},
#     {"name":"raj","score":68}
#     ]
# for student in school:
#     print(student["name"],":",student["score"])

# write a file
# with open("sample.text","w") as file:
#     file.write("hello from python!")

# with open("sample.text","a") as file:
#     file.write(" welcome to vs code")

# with open("sample.text","r") as file:
#     content = file.read()
#     print(content)

entry = input("Write a diary entry: ")

with open("sample.text", "a") as file:
    file.write(entry + "\n")