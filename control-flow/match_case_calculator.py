num1 = float( input("Enter the first number: "))
num2 = float( input("Enter the second number: "))
operat = input("Choose the operation (+, -, *, /):")

match operat :
    case "+":
        result = num1 + num2
     
    case "-":
        result = num1 - num2
        
    case "*":
        result = num1 * num2
        
    case "/":
        result = num1 / num2 if num2 != 0 else "You cannot divid by zero"
        
    case _:
        result = "Invalid input"
        
print(f"The result is {result}")    
