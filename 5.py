print("*---*---*--- Decimal to Octal Conversion ---*---*---*\n")

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


octal_number = ''
decimal_number = int(input_value)

if decimal_number == 0:
    octal_number = '0'

while decimal_number > 0:
    remainder = decimal_number % 8
    octal_number = str(remainder) + octal_number
    decimal_number = decimal_number // 8


print(f"The octal value of {input_value} is {octal_number}\n")

print("*---*---*--- Decimal to OCtal Conversion ---*---*---*")