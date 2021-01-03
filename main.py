def intToBinary(n):
    '''
    Converts an integer 'n' into it's Binary equivalent.

    USAGE:

    print(intToBinary(501))

    OUTPUT:

    111110101
    '''
    # Initializing the variable to hold the coded value
    code = ""
    # Loop until you reach the most significant bit
    while n / 2 > 0:
        # Add remainder as the least significant digit
        digit = n % 2
        # Consider the quotient for the next iteration
        n = int(n / 2)
        code = str(digit) + code
    return code

def intToOctal(n):
    '''
    Converts an integer 'n' into it's Octal equivalent.

    USAGE:

    print(intToOctal(501))

    OUTPUT:

    1F5
    '''
    # Initializing the variable to hold the coded value
    code = ""
    # Loop until you reach the most significant bit
    while n / 8 > 0:
        # Add remainder as the least significant digit
        digit = n % 8
        # Consider the quotient for the next iteration
        n = int(n / 8)
        code = str(digit) + code
    return code

def intToHexDecimal(n):
    '''
    Converts an integer 'n' into it's Hexadecimal equivalent.

    USAGE:

    print(intToHexDecimal(501))

    OUTPUT:

    1F5
    '''
    # Initializing the variable to hold the coded value
    code = ""
    # Loop until you reach the most significant bit
    while n / 16 > 0:
        # Add remainder as the least significant digit
        digit = n % 16
        # Consider the quotient for the next iteration
        n = int(n / 16)
        if digit < 10:
            char = str(digit)
        elif digit == 10:
            char = "A"
        elif digit == 11:
            char = "B"
        elif digit == 12:
            char = "C"
        elif digit == 13:
            char = "D"
        elif digit == 14:
            char = "E"
        else:
            char = "F"
        code = char + code
    return code

# Testing the functions
print(501, intToHexDecimal(501), intToBinary(501), intToOctal(501))
print(4253, intToHexDecimal(4253), intToBinary(4253), intToOctal(4253))
print(16, intToHexDecimal(16), intToBinary(16), intToOctal(16))

# Converts a input string into it's binary, octal and hexadecimal equivalent
text = input("Enter a string: ")

# Intializing the output variables
binaryText = ""
octalText = ""
hexText = ""

# Looping throught every character
for char in text:
    binaryText = binaryText + intToBinary(ord(char)) + " "
    octalText = octalText + intToOctal(ord(char)) + " "
    hexText = hexText + intToHexDecimal(ord(char)) + " "

# Printing the output
print("Binary Equivalent String: ", binaryText)
print("Octal Equivalent String: ", octalText)
print("Hexadecimal Equivalent String: ", hexText)