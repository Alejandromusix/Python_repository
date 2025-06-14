import random
def main():
    while True:
     #Values of the dice
     dice = [1, 2, 3, 4, 5, 6]
     #Launch the dice
     def choice():
         result = random.choice(dice)
         print("The result is: ", result)
     try:
      dec = input("Do you wanna run the dice? y/n ")
     except ValueError:
      print("Answer 'y' or 'n'")
#User choices
     if dec == "y":
      choice()
     else:
       break
     try:
       again = input("Do you want to run another dice? y/n ")
     except ValueError:
       print("Please, answer 'y' or 'n'")
       
     if again == "y":
       choice()
     else:
       break
     
main()
