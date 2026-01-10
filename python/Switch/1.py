num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

oprator = input("Enter operation (+, -, *, /): ")

match oprator:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Error: Invalid operation")