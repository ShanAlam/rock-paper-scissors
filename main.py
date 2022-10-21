import random

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


# Storing ASCII art in a list
all_choices = [rock, paper, scissors]

# Header
print("Welcome to The Rock, Paper, Scissors Game! \n")

# Taking a choice from user
human_choice = int(input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors \n"))

# Checking if the choice is valid
if human_choice < 0 or human_choice > 2:
  print("Invalid input, You lose :(")

# If the choice is valid, the program proceeds
else:

  # Print ASCII art corresponding to users choice
  print(all_choices[human_choice])
  # Use random module to choose a move for computer
  computer_choice = random.randint(0,2)
  print("The computers choice was: \n")
  # Print random integer choice
  print(computer_choice)
  # Print ASCII art corresponding to random choice
  print(all_choices[computer_choice])
  
  # The following logic for the game
  if human_choice == 0 and computer_choice == 2:
    print("Well done! You won!")
  
  elif human_choice == 1 and computer_choice == 0:
    print("Well done! You won!")
  
  elif human_choice == 2 and computer_choice == 1:
    print("Well done! You won!")
  
  elif human_choice == computer_choice:
    print("It was a draw!")
  
  else:
    print("Oh no! You lost :(")
      