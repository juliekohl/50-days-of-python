# Class, Attributes, Constructors (__init__(self)) and Methods
from typing import Any


class User:

    def __init__(self, user_id: str, username: str) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user: Any) -> None:
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Julie"
user_1 = User("001", "Julie")
print(user_1.id)
print(user_1.username)

user_2 = User("002", "César")
print(user_2.id)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Quiz Project
# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
