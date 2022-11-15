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

# Exercicse

two_digits = input("Type a two digit number: ")

first_digit = int(two_digits[0])
second_digit = int(two_digits[1])

result_digits = first_digit + second_digit

print(result_digits)
