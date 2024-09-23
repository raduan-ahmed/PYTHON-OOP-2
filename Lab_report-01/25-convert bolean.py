def convert_decimal(number):
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    return binary, octal, hexadecimal

decimal_number = 345

binary, octal, hexadecimal = convert_decimal(decimal_number)
print(f"The decimal value of {decimal_number} is:")
print(f"{binary} in binary.")
print(f"{octal} in octal.")
print(f"{hexadecimal} in hexadecimal.")
