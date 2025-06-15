import random
def main():
    print("Guess the number")

    try:
     first = int(input("Write your first number: "))
     second = int(input("Write your second number: "))
    except ValueError:
     print("Please write a valid value")
     return main()

    number = random.randint(first, second)
    
    
    while True:
     try:
      answer = int(input("What number do you think it is? "))
     except ValueError:
       print("Write a number")
 
     if number > answer:
        print("Too low")
     elif number < answer:
        print("Too high")
     else:
        print(f"You did it: {answer} is equal to {number}")
        break

    oportunity = input("Do you want to play again? y/n ").strip()
    try:
     if oportunity == "y":
       main()
     elif oportunity == "n":
        print("Thanks for playing!")
    except ValueError:
       print("Please write one of the options")
    
main()
