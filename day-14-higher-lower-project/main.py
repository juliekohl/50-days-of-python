import random
from typing import Any, Dict
from game_data import data
from art import logo, vs
from replit import clear


def get_random_account() -> Dict[Any, str]:
    """Get data from random account"""
    return random.choice(data)


def format_data(account: Dict[str, str]) -> str:
    """Format account into printable format: name, description and country"""
    name: str = account["name"]
    description: str = account["description"]
    country: str = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess: str, a_followers: str, b_followers: str) -> Any:
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game() -> None:
    print(logo)
    score: int = 0
    game_should_continue: bool = True
    account_a: Dict[Any, str] = get_random_account()
    account_b: Dict[Any, str] = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess: str = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count: str = account_a["follower_count"]
        b_follower_count: str = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()

# 1. Generate a random account from the game data.

# 2. Format account data into printable format.

# 3. Ask user for a guess.

# 4. Check if user is correct.
## 5. Get follower count.
## 6. If Statement

# 7. Feedback.

# 8. Score Keeping.

# 9. Make game repeatable.

# 10. Make B become the next A.

# 11. Add art.

# 12. Clear screen between rounds.
