num1 = int( input("Enter the first number: "))
num2 = int( input("Enter the second number: "))
operat = input("Choose the operation (+, -, *, /):")

match operat :
    case "+":
        result = num1 + num2
        print("The result is ", result)
    case "-":
        result = num1 - num2
        print("The result is ", result)
    case "*":
        result = num1 * num2
        print("The result is ", result)
    case "/":
        if num2 == 0:
            print("This gives the result of infinity")
        else:
            result = num1 / num2
            int("The result is ", result)
        
    case _:
        print("Invalid input")
        
