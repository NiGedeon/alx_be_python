def perform_operation(num1, num2, operation):
        if (operation == "add"):
            result = num1 + num2
            print(result)
        elif(operation == "subtract"):
            result = num1 - num2
            print(result)
        elif(operation == "multiply"):
            result = num1 * num2
            print(result)
        elif(operation == "divide") :
            result = num1 /num2 if num2 != 0 else "It's impossible to divide a number by zero."
            print(result)
        else :
            result = "Invalid input"
            print(result)
        return result
