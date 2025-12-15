
# def chatbot():
#     print("hello! am chatbot")
# name=input("whats ur name?")
# print("hello",name,"nice to meet u")

# def chatbot():
#     print("hello am chatbot, type bye to exit")

#     while True:
#         mesg = input("you:")
#         if mesg == "bye":
#             print("chatbot:","good bye!")
#             break
#         else:
#             print("chatbot: you said")

# chatbot()

# def chatbot():
#     print("hello am chatpy, type bye to exit.")
#     while True:
#         mesg = input("you:")
#         if mesg == "bye":
#             print("chatpy: good bye!")
#             break
#         elif "how are you" in mesg:
#             print("chatpy: i am fine<tqq>")
#         else:
#             print("chatpy: okk")
# chatbot()

# while True:
#     item = input("enter done or finish:")
#     if item == "done":
#         break
#     cash = input("how much did u spend")
#     with open("sample.text","a") as file:
#         file.write(item + "$"+cash + "/n")
# print("all set.")

# while True:
#     item = input("enter are you done or finish:")
#     if item == "done":
#         break
#     cash = ("how much do u spend:")
#     with open("sample.text","a") as file:
#         file.write(item + "$" + cash + "/n")

# with open("sample.text","r") as file:
#   print("this is the list of exences ad cash spent:")
#   print(file.read())
    
# def log_expense():
#     while True:
#         item = input("Enter an item (or 'done' to finish): ")
#         if item == "done":
#             break
#         amount = input("How much did you spend on it? ")
#         with open("expenses.txt", "a") as file:
#             file.write(item + ": $" + amount + "\n")
    
#     print("All expenses saved!")

# def view_expenses():
#     with open("expenses.txt", "r") as file:
#         print("Here are your expenses:")
#         print(file.read())

# log_expense()
# view_expenses()

# modules
# import turtle
# import random
# from time import sleep

# print(random.choice(["heads","tails"]))
#print(coin)

# import math
# print(math.sqrt(399))
# print(math.pi)

# from datetime import datetime
# print(datetime.now())
# print(now)

# import random

# die1 = random.randint(1,6)
# die2 = random.randint(1, 6)
# print("We rolled a die1", die1)
# print("we rolled a die2",die2)

# import turtle
# pen = turtle.Turtle()
# #sleep(4)
# pen.forward(50)
# pen.right(35)
# pen.backward(80)
# pen.left(35)
# sleep(4)

# import turtle
# pen = turtle.Turtle()
# for _ in range(4):
#  pen.forward(70)
#  pen.right(50)

# turtle.done()

# import turtle

# pen = turtle.Turtle()
    
# pen.color("red")
# for i in range(50):
#     pen.forward(i * 5)
#     pen.right(45)
#     sleep(5)

# import turtle

# pen = turtle.Turtle()

# pen.color("blue")        # Change color
# sides = 8                # Change number of sides
# angle = 360 / sides      # Adjust angle based on sides

# for _ in range(sides):
#     pen.forward(80)
#     pen.right(angle)

# print("🌡️ Welcome to the Temperature Converter!")
# print("Choose a conversion:")
# print("1: Celsius to Fahrenheit")
# print("2: Fahrenheit to Celsius")
# print("3: Celsius to Kelvin")
# print("4: Kelvin to Celsius")
# print("5: Fahrenheit to Kelvin")
# print("6: Kelvin to Fahrenheit")
# choice = input("Enter your choice (1-6): ")
# temp = float(input("Enter the temperature to convert: "))

# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32

# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9

# def celsius_to_kelvin(c):
#     return c + 273.15

# def kelvin_to_celsius(k):
#     return k - 273.15

# def fahrenheit_to_kelvin(f):
#     return (f - 32) * 5/9 + 273.15

# def kelvin_to_fahrenheit(k):
#     return (k - 273.15) * 9/5 + 32

# if choice == "1":
#     result = celsius_to_fahrenheit(temp)
#     print("{}°C is {:.2f}°F".format(temp, result))
# elif choice == "2":
#     result = fahrenheit_to_celsius(temp)
#     print("{}°F is {:.2f}°C".format(temp, result))
# elif choice == "3":
#     result = celsius_to_kelvin(temp)
#     print("{}°C is {:.2f}K".format(temp, result))
# elif choice == "4":
#     result = kelvin_to_celsius(temp)
#     print("{}K is {:.2f}°C".format(temp, result))
# elif choice == "5":
#     result = fahrenheit_to_kelvin(temp)
#     print("{}°F is {:.2f}K".format(temp, result))
# elif choice == "6":
#     result = kelvin_to_fahrenheit(temp)
#     print("{}K is {:.2f}°F".format(temp, result))
# else:
#     print("Invalid choice. Please run the program again.")

# Print multipes of 2
# output : 2 * 1 = 2
# for i in range(1,11,1):
#     print("2","*",i,"=",2*i)

# num = [1,2,3,4,5]
# for n in num:
#     if n == 3:
#         break
#     else:
#      print("red 345")

# import random

# quotes = {
#     "motivational": [
#         "Believe you can and you're halfway there. – Theodore Roosevelt",
#         "It always seems impossible until it's done. – Nelson Mandela",
#         "The best way to get started is to quit talking and begin doing. – Walt Disney",
#     ],
#     "funny": [
#         "I'm not arguing, I'm just explaining why I'm right. – Unknown",
#         "Why don’t scientists trust atoms? Because they make up everything!",
#         "I'm on a seafood diet. I see food and I eat it. – Unknown",
#     ],
#     "tech": [
#         "Talk is cheap. Show me the code. – Linus Torvalds",
#         "Programs must be written for people to read. – Harold Abelson",
#         "First, solve the problem. Then, write the code. – John Johnson",
#     ]
# }
# print("💬 Welcome to the Quote Machine!")
# print("Available categories: motivational, funny, tech")

# while True:
#     category = input("\nWhich type of quote would you like? ").strip().lower()
    
#     if category in quotes:
#         quote = random.choice(quotes[category])
#         print("\n👉 {}".format(quote))
#     else:
#         print("❌ That category doesn't exist. Try again!")

#     again = input("\nWant another one? (y/n): ").strip().lower()
#     if again != 'y':
#         print("👋 See you next time! Stay inspired!")
#         break

# import random

# print("🎉 Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100. Can you guess it?")
# secret_number = random.randint(1, 100)
# attempts = 0
# while True:
#     guess = int(input("Take a guess: "))
#     attempts += 1
#     if guess < secret_number:
#         print("Too low! But nice try! 🔽")
#     elif guess > secret_number:
#         print("Too high! You're flying too close to the sun! 🔼")
#     else:
#         print(f"🎉 Congrats! You guessed the number in {attempts} attempts!")
#         break
#     best_score = None

# play_again = "yes"
# while play_again.lower() == "yes":
#     # (Your guessing game here)

#     if best_score is None or attempts < best_score:
#         best_score = attempts
#         print(f"🏅 New record! Fewest attempts: {best_score}")

#     play_again = input("Want to play again? (yes/no): ")
#     if play_again.lower() != "yes":
#         print("Thanks for playing! Come back soon!")