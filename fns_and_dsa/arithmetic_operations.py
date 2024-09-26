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
            if num2 == 0:
                result = "Error: Division by zero is not possible"
                print(result)
            else:
                result = num1 /num2 
                print(result)
        else :
            result = "Invalid input"
            print(result)
        return result
