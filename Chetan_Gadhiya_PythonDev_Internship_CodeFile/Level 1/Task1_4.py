def calculator():
    print("Welcome to the basic Calculator!")

    try:
        num1 = float(input("Enter Number 1: "))
        operator = input("Enter operator from (+,-,*,/,%): ")
        num2 = float(input("Enter Number 2: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Zero Devision Error!")
                return
            else:
                result = num1 / num2
        elif operator == "%":
            if num2 == 0:
                print("Modulus by zero is not allowed!")
                return
            else:
                result = num1 % num2
        else:
            print("Invalid operator")

        print(f"The result of {num1} {operator} {num2} is : {result}")

    except ValueError:
        print("Please Enter a valid number")


calculator()
