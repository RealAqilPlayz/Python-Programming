my_name = input("Enter your name: ")
print("Welcome back, " + my_name + "!")
print("The calculator app has been launched!")

result = 0
first_calculation = True

while True:

    if first_calculation:
        num1 = float(input("Enter a number: "))
        first_calculation = False
    else:
        num1 = result

    opr = input("Enter an operator (+, -, *, /, %, ^): ")
    num2 = float(input("Enter a number: "))

    if opr == "+":
        result = num1 + num2

    elif opr == "-":
        result = num1 - num2

    elif opr == "*":
        result = num1 * num2

    elif opr == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Division by zero error! NaN")

    elif opr == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Division by zero error! NaN")

    elif opr == "^":
        result = num1 ** num2


    print("Current Result:", result)















