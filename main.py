import art
from game_data import data
import random



def format_data(account):
    """Format the account data intro printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    print(f"{account_name}, a {account_description}, from {account_country}")


print(art.logo)

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(f"Compare B: {format_data(account_b)}.")

