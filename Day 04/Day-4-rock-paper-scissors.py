rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
me = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if me >= 3 or me < 0:
    print("You typed an invalid number, you lose!")
else:
    print(choices[me])

    computer = random.randint(0, len(choices) - 1)
    print(f"Computer chose: \n {choices[computer]}")

    if (me == 0 and computer == 2):
        print("You win!")
    elif (me == 2 and computer == 0):
        print('You lose')
    elif (me > computer):
        print("You win!")
    elif (me < computer):
        print("You lose")
    elif (me == computer):
        print("It's a draw")
