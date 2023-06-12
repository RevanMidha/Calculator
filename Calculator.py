import Addition
import Subtraction
import Multiplication
import Division
import power

# This is to present a menu to the user
print("Select operation.")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power\n")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")
    print()

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Addition.add(num1, num2))
            print()

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))
            print()

        elif choice == '3':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))
            print()

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", Division.divide(num1, num2))
                print()
            except:
                print("Division by zero not allowed\n")

        elif choice == '5':
            print(num1, "^", num2, "=", Power.power(num1, num2))
            print()
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        print()
        
        if next_calculation in 'yY':
            print("Thank for using our calculator!\n")
            break
    else:
        print("Invalid Input\n")
