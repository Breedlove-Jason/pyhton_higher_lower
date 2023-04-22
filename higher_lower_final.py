from art import logo, vs
from game_data import data
import random
from os import system


def format_data(account):
    """Take the account data and return the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Display art
score = 0
account_b = random.choice(data)

game_should_continue = True
# Make the game repeatable.
while game_should_continue:

    # Generate a random account from the game data.
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get follower count of each account.
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # Clear the screen between rounds.
    system("clear")
    print(logo)
    # Give user feedback on their guess.
    # If user is correct, add 1 to the score.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")
    else:
        print(f"Sorry that's wrong! Final score: {score}")
        game_should_continue = False
