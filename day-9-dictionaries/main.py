# Dictionary
from typing import Dict, Any, List
from replit import clear
from art import logo

# programming_dictionary: Dict[str, str] = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# Retrieve items
# programming_dictionary["Function"]
# print(programming_dictionary["Function"]) # retrive the value

# Add nem item
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary) # add new key: value

# Create an empty dictionary
# empty_dictionary: Dict[Any, Any] = {}
# print(empty_dictionary) # {}

# Edit an item
# programming_dictionary["Bug"] = "Update an item, this bug here!"
# print(programming_dictionary) # Bug is updated

# Loop through a dictionary
# for thing in programming_dictionary:
#     print(thing) # Bug Function - return keys

# for key in programming_dictionary:
#     print(programming_dictionary[key]) # return values


# Exercise Grading Program
# student_scores: Dict[str, int] = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 67,
# }
#
# student_grades: Dict[str, str] = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
#
# print(student_grades)

# Nesting Lists and Dictionaries
# Nesting
# capitals: Dict[str, str] = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }
# print(capitals["France"]) # Paris return valu

# Nesting a List in a Dictionary
# travel_log: Dict[str, Any] = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# print(travel_log["Germany"]) # return values

# Nesting Dictionary in a Dictionary
# travel_log: Dict[str, Any] = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
# print(travel_log["France"]) # return values

# Nesting Dictionaries in Lists
# travel_log: List[Dict[str, object]] = [
#     {
#       "country": "France",
#       "cities_visited": ["Paris", "Lille", "Dijon"],
#       "total_visits": 12,
#     },
#     {
#       "country": "Germany",
#       "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#       "total_visits": 5,
#     },
# ]
# print(travel_log[0]) # return value
# print(travel_log[0]["cities_visited"]) # return value

# Exercise Dictionary in List
# travel_log: List[Dict[str, object]] = [
#     {
#       "country": "France",
#       "visits": 12,
#       "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#       "country": "Germany",
#       "visits": 5,
#       "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
# def add_new_country(name: str, visit_count: int, cities_visited: Any) -> None:
#   new_country: Dict[Any, Any] = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)
#
# add_new_country(name="Russia", visit_count=2, cities_visited=["Moscow", "Saint Petersburg"])
# print(travel_log)

# Project Blind Auction
print(logo)

bids: Dict[Any, Any] = {}
bidding_finished: bool = False


def find_highest_bidder(bidding_record: Dict[str, int]) -> None:
    highest_bid: int = 0
    winner: str = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name: str = input("What is your name?: ")
    price: int = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue: str = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

