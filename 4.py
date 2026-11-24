print("*---*---*--- Decimal to Binary Conversion ---*---*---*\n")

input_value = ""

while True:
    input_value = input("Enter a Decimal number to convert: ")

    # check if the input is empty

    if input_value == "":
        print("Enter something please.\n")
        continue

    # make sure the input is a number

    is_valid = True

    for char in input_value:
        if char not in '0123456789':
            is_valid = False

    # check if it is still valid

    if is_valid:
        break # stop the while loop
    else:
        print("The inputted value is invalid.\n")

binary_number = ''
decimal_number = int(input_value)

if decimal_number == 0:
    binary_number = '0'

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2

print(f"The binary value of {input_value} is {binary_number}\n")

print("*---*---*--- Decimal to Binary Conversion ---*---*---*")