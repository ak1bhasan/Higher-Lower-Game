import art
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)


    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Compare B: {format_data(account_b)}.")


        guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

        print("\n" * 20)
        print(art.logo)

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"\nYou're right! 🎉 Current score: {score}\n")
        else:
            print(f"\n❌ Sorry, that's wrong! Final score: {score}\n")
            game_should_continue = False

game()
while input("Play again? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    game()


