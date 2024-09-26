def perform_operation(num1, num2, operation):
        match(operation):
            case "add":
                result = num1 + num2
            case "subtract":
                result = num1 - num2
            case "multiply":
                result = num1 * num2
            case "divide" :
                result = num1 /num2 if num2 != 0 else "It's impossible to divide a number by zero." 
            case _ :                                                                                                            result = "Invalid input"                                                                                return result
