def convert_temperature(temp, unit):
    if unit == 'C' or unit == 'c':
        return (temp * 9/5) + 32
    if unit == 'F' or unit == 'f':
        return (temp - 32) * 5/9

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ")

converted = convert_temperature(temp, unit)

print("Converted temperature:", converted)
