
import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo)


def check_answer(guess, answer, turns):
  if guess < answer:
    print("Too low.")
    return turns - 1
  elif guess > answer:
    print("Too high.")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}.")

def set_difficulty ():
    choice = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
      return EASY_LEVEL
    elif choice == 'hard':
      return HARD_LEVEL

def game():
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 & 100.")
  answer = random.randint(1, 100)
  
  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess= guess, answer=answer, turns=turns)
    if turns == 0:
      print("You've run out of guesses, you loss.")
      return
    elif guess != answer:
      print("Guess again.")
game()