from typing import List, Any


class QuizBrain:

    def __init__(self, q_list: List[Any]) -> None:
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: List[Any] = q_list

    def still_has_questions(self) -> int:
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        current_question: Any = self.question_list[self.question_number]
        self.question_number += 1
        user_answer: str = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

