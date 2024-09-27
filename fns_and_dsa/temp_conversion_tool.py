fahrenheit_to_celsius_fact = 5 / 9
celsius_to_fahrenheit_fact = 9 / 5
default = 32


def convert_to_celsius(fahrenheit):
    return (fahrenheit - default) * fahrenheit_to_celsius_fact


def convert_to_fahrenheit(celsius):
    return celsius * celsius_to_fahrenheit_fact + default


def main():
    
    temp_input = float(input("Enter the temperature to convert: "))


    temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


    if temp == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    elif temp == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

