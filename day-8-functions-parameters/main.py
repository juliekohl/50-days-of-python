# Create a simple function called greet()
# def greet() -> None:
#     print('star function')
#     print('Helo from greet!')
#     print('end function')
#
#
# greet()

# Create a function that allows for input
# def greet_with_input(name: str) -> None:
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
#
# greet_with_input("Julie")

# Create a function with keyword arguments
# def greet_with(name: str, location: str) -> None:
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with(name="Julie", location="Paris")

# Exercise Paint area calculator
# import math
#
# def paint_calc(height: int, width: int, cover: int) -> None:
#     num_cans = (height * width) / cover
#     round_up_cans = math.ceil(num_cans)
#     print(f"You'll need {round_up_cans} cans of paint.")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise Prime Number Checker
# def prime_checker(number: int) -> None:
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Project Caesar Cipher
# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text: str, shift_amount: int) -> None:
#   # TODO-1.2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.
#   # e.g.
#   # plain_text = "hello"
#   # shift = 5
#   # cipher_text = "mjqqt"
#   # print output: "The encoded text is mjqqt"
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")
#
# # TODO-2: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text: str, shift_amount: int) -> None:
#   # TODO-2.1: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
#
#
# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

# Refactoring
# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> None:
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")
#
#
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# Improvement
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> None:
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo

print(logo)

# TODO-1: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
