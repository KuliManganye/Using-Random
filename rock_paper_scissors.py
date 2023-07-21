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
import random

map = [rock, paper, scissors]

# get user input and convert that into integers as with lists, we are dealing with integers. 
# Therefore rock = 0, paper = 1 and scissors = 2

user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissoes \n"))

# print user input
user_choice = map[user]
print(f"You choose: \n {user_choice}")

# generate computer choice and shuffle it. Then print it
items = len(map)
random_choice = random.randint(0,2)
computer_choice = map[random_choice]
print(f"Computer chose: \n {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")