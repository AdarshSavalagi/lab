def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        power += 1
        binary //= 10
    return decimal

def octal_to_hexadecimal(octal):
    decimal = 0
    power = 0
    while octal > 0:
        last_digit = octal % 10
        decimal += last_digit * (8 ** power)
        octal //= 10
        power += 1

    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        last_digit = decimal % 16
        hexadecimal = hex_digits[last_digit] + hexadecimal
        decimal //= 16
    return hexadecimal

# Binary to Decimal Conversion
binary = input("Enter a binary number: ")
decimal = binary_to_decimal(int(binary))
print(f"The decimal representation of {binary} is: {decimal}")

# Octal to Hexadecimal Conversion
octal = input("Enter an octal number: ")
hexadecimal = octal_to_hexadecimal(int(octal))
print(f"The hexadecimal representation of {octal} is: {hexadecimal}")
