# len
# print(len("Hello"))  # 5
# print(len(12345))  # error

# Primitive Data Types

# String
# "Hello"
# print("Hello"[0]) #H
# print("Hello"[4]) #o

# print("123" + "345") #"123345"
# print("Hello" + "world") #"Helloworld"

# Integer
# print(123 + 345) #468

# 123_456_789

# Float
# 3.14159
# 3141.59

# Boolean
# True
# False

# Type checking and conversion

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.") # juliana 7

# a = str(123)
# print(type(a)) # str type() show type of

# a = float(123)
# print(type(a)) # float

# print(70 + float("100.5")) # 107.5
# print(str(70) + str(100)) # 70100

# str() change to string
# float() change to float

# Exercise

# two_digits = input("Type a two digit number: ")
#
# first_digit = int(two_digits[0])
# second_digit = int(two_digits[1])
#
# result_digits = first_digit + second_digit
#
# print(result_digits)

# Mathematical Operations
#
# 3 + 5 # 8
# 5 - 3 # 2
# 3 * 5 # 15
# 6 / 3 # float 2.0
# 2 ** 2 # 4
# 2 ** 3 # 8
#
# PEMDASLR
# ()   # Parentheses
# **   # Exponents
# * /  # Multiplication Division
# + -  # Addition Subtraction
#
# print(3 * 3 + 3 / 3 - 3) # 7.0
# print(3 * (3 + 3) / 3 - 3) # 3.0
#
# Exercises
#
# height = input("Enter your height in m: ")
# weight = input("Enter your height in kg: ")
#
# height_num = float(height)
# weight_num = int(weight)
#
# bmi = weight_num / height_num ** 2
#
# result = int(bmi)
# print(result)
#
# F Strings

# print(8 / 3) #2.66666666666665
# print(int(8 / 3)) # 2 int()
# print(round(8 / 3)) # 3 round()
# print(round(8 / 3, 2)) # 2.67 round()
# print(type(8 // 3)) # 2 int type()
# print(type(8 / 3)) #2.66... float type()
#
# User scores a point
# score += 1
# score -= 1
# score *= 1
# score /= 1
#
# score = 0
# height = 1.57
# isWinning = True
#
# print(f"Yorur score is {score}, your height is {height}, and you are winning is {isWinning}!") # Yorur score is 0, your height is 1.57, and you are winning is True!
#
# Exercises
#
# age = input("What is your current age? ")
#
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left. So enjoin your life!")
#
# print(6 + 4 / 2 - (1 * 2)) # 6.0
# a = int("5") / int(2.7) # 2.5
# print(a)
#
# Project Calculator
#
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)

percent_tip = tip_int / 100
bill_with_tip = bill_float * percent_tip
total_bill = bill_float + bill_with_tip
bill_per_person = round(total_bill / people_int, 2)
final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_bill}")
