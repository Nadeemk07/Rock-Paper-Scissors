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
choice=int(input("What do you want to Choose 0 for rock, 1 for paper, 2 for scissors\n"))
print("You choose\n")

if(choice==0):
  print(rock)
elif(choice==1):
  print(paper)
elif(choice==2):
  print(scissors)
list=[rock,paper,scissors]
computer_choice=random.choice(list)
print("Computer choose")  
print(computer_choice)

if(choice==0 and computer_choice==rock):
  print("No one wins")
if(choice==0 and computer_choice==paper):
  print("You Lose")
if(choice==0 and computer_choice==scissors):
  print("You won")


if(choice==1 and computer_choice==rock):
  print("You won")
if(choice==1 and computer_choice==paper):
  print("Tie")
if(choice==1 and computer_choice==scissors):
  print("You lose")   


if(choice==2 and computer_choice==rock):
  print("You lose")
if(choice==2 and computer_choice==paper):
  print("You won")  
if(choice==2 and computer_choice==scissors):
  print("Tie")  