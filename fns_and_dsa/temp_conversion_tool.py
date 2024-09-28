FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():

    temp_input = float(input("Enter the temperature to convert: "))


    temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


    if temp == 'F':
        converted_temp = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {converted_temp:.2f}°C")
    elif temp == 'C':
        converted_temp = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
