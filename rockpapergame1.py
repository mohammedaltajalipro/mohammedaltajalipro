import random
print("rock , paper , scissors ")
choice = ["rock" , "paper" , "scissors" ]

while True:

 while True:
  user_input = input("Do you want to play? (yes/no): ").lower()

  if user_input == "yes":
   break
  elif user_input == "no":
   print("Thanks for playing!")
   exit()
  else:
   print("Invalid input. Please enter 'yes' or 'no'.")

 user_score = 0
 computer_score = 0

 for round in range(5):
  print("round",round+1)

  while True:
    user = input("Enter your choice: ")

    if user in choice:
        break

    print("Invalid choice!")

  computer = random.choice(choice)
  print("Computer chose:", computer)

  #user winning conditions
  if user == computer:
   print("Tie")
  elif user == "paper" and computer == "rock":
   print("user wins")
   user_score +=1
  elif user == "scissors" and computer == "paper":
   print("user wins")
   user_score +=1
  elif user == "rock" and computer == "scissors":
   print("user wins")
   user_score +=1

  #computer winning conditions
  elif computer == "paper"and user == "rock":
   print("computer wins")
   computer_score +=1
  elif computer == "scissors" and user == "paper":
   print("computer wins")
   computer_score +=1
  elif computer == "rock" and user == "scissors":
   print("computer wins")
   computer_score +=1

  print("score -->user:",user_score,"computer:",computer_score)

 print("\n ==========FINAL SCORES===========")
 print("user_score:",user_score)
 print("computer_score:",computer_score)

 if user_score >computer_score:
  print("Congratulations! You won the game!")
 elif user_score <computer_score:
  print("Computer wins the game! Better luck next time.")
 else:
  print('The game is a tie')

 play_again = input("Play again? (yes/no): ").lower()

 if play_again != "yes":
  print("Thanks for playing!")
  break
