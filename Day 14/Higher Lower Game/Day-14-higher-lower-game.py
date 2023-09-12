
# Import art to print logo
from art import logo, vs
# Extract data from game_data file
from game_data import data
dataset = data

# random choice function
import random
def random_choice(dataset):
  value = random.choice(dataset)
  return value
  
# Format function to print all extracted data
def format(account):
  acount_name = account["name"]
  acount_description = account["description"]
  acount_country = account["country"]
  return f"{acount_name}, a {acount_description}, from {acount_country}"


# compare their follower. compare A and Against B
def compare(user_answer,A_followers, B_followers):
  if A_followers > B_followers:
    return user_answer == 'a'  
  else : 
    return user_answer == 'b'

# Display Art
print(logo)
score = 0
flag = True
index_B = random_choice(dataset)

#Make code repeateable
while flag :
  # Choose 2 random person  from game data to compare
  
  # Making account / index B become the next account A
  index_A = index_B
  index_B = random_choice(dataset)
  
  if (index_A == index_B):
    index_B = random_choice(dataset)
    
  print(f"Compare A: {format(index_A)}.")
  print(vs)
  print(f"Against B: {format(index_B)}.")
  
# Ask user to answer "Who has more followers?: Type 'A' or 'B'"  
  guess = input("Who has more followers?: Type 'A' or 'B': ").lower()
  
# Check if user type right answer then continue the game and if give wrong answer the end the game and show final score
  followers_A = index_A["follower_count"]
  followers_B = index_B["follower_count"]
  
# Final Result
  is_correct = compare(user_answer = guess, A_followers = followers_A, B_followers = followers_B)
  
  if is_correct :
    score += 1
    print(f"You're right! current score: {score}")
  else:
    flag = False
    print(f"Sorry, that's wrong. Final Score: {score}")
  
     

