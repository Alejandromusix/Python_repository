def add(x, y):
   return x + y

def subs(x, y):
   return x - y

def mult(x, y):
   return x * y

def div(x, y):
   return x / y

def main():
   while True:
     print("Choose an operator:")
     print("1 = Addition")
     print("2 = Substraction")
     print("3 = Multiplication")
     print("4 = Division")

     choose = int(input("Choose a number: "))
     if choose in (1, 2, 3, 4):
         try:
             x = float(input("First number: "))
             z = float(input("Second number: "))
         except ValueError:
           print("Please, write a number")
           continue

     if choose == 1:
        print(x, "+", z, "=", add(x, z))

     elif choose == 2:
        print(x, "-", z, "=", subs(x, z))

     elif choose == 3:
        print(x, "*", z, "=", mult(x, z))

     elif choose == 4:
        print(x, "/", z, "=", div(x, z))



main()
