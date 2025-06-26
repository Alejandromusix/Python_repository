def main():
    while True:
        print("Temperature Conversion")
        print("1.Celsius to Fahrenheit 2.Fahrenheit to Celsius 3.Celsius to Newton 4.Fahrenheit to Newton")
        try:
            user_choice = int(input("Your choice: "))
        except ValueError:
            print("Enter a compatible value")
            break
        if user_choice >= 5:
           print("Please, write a compatible value")
           break

        temperature = float(input("Enter the temperature you want to convert: "))
        if user_choice == 1:
          r1 =  temperature * 9/5 + 32
          print(f"{temperature} C° in fahrenheit is {r1} F°")
        elif user_choice == 2:
           r2 = (temperature - 32) * 5/9
           print(f"{temperature} f° in celsius is {r2} C°")
        elif user_choice == 3:
            r3 = temperature / 3.03030303 
            print(f"{temperature} C° in Newton is {r3} °N")
        elif user_choice == 4:
            r4 = (temperature - 32) / 5.45454555
            print(f"{temperature} f° in fahrenheit is {r4} °N")

        again = input("Do you want to calculate another thing? y/n ")
        if again == "y":
          continue
        else:
          break
main()
