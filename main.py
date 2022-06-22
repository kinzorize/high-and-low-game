# high low game project

from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)

# create input for A and B 
def random_choice():
  return random.choice(data)


# create a random comparision form the game_data
def compare_followers(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name}, {description}, from {country}"
  print(f"{name}, {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_choice()
  account_b = random_choice()
  while game_should_continue:
    account_a = account_b
    account_b = random_choice()
    while account_a == account_b:
      account_b == random_choice()
      print(f"Compare A: {compare_followers(account_a)}")
      print(vs)
      print(f"Against B: {compare_followers(account_b)}")
      guess = input("Who has more followers, Type 'A' or 'B': ").lower()
      a_follower_count = account_a["follower_count"]
      b_follower_count = account_b["follower_count"]
      is_correct = check_answer(guess, a_follower_count, b_follower_count)
      clear()
      print(logo)
      if is_correct:
        score += 1
        print(f"You're right! current score: {score}")
      else:
        game_should_continue = False
        print(f"Sorry that's wrong, Final score: {score}")
    
game()
# follower_name, follower_description, follower_country

# compare the followers
