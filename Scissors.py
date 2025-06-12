import random
def main():
    while True:
      try:
        user = input("Choose an option (paper, scissors or rock): ").strip()
      except ValueError:
         print("Please write one of the options")
      possible_action = ["paper", "rock", "scissors"]
      computer_action = random.choice(possible_action)

      print(f"You choose {user} and the computer choose {computer_action}")

      if user == computer_action:
         print("It's a tie")
      elif user == "paper" and computer_action[1]:
         print("You win")
      elif user == "rock" and computer_action[2]:
         print("You win")
      elif user == "scissors" and computer_action[0]:
         print("You win")
      else:
         print("You lose")    

      play = input("Do you want to play again y/n: ")

      if play == "n":
        break
      else:
        continue
    
main()
