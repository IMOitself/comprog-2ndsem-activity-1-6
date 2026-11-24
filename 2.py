print("*---*---*--- Octal to Decimal Conversion ---*---*---*\n")

input_value = ""

while True:
    input_value = input("Enter an Octal number to convert: ")

    # check if the input is empty

    if input_value == "":
        print("Enter something please.\n")
        continue

    # make sure the input is only 0 to 7

    is_valid = True

    for char in input_value:
        if char not in '01234567':
            is_valid = False

    # check if it is still valid

    if is_valid:
        break # stop the while loop
    else:
        print("The inputted value is invalid.\n")
               

octal_list = list(input_value)
octal_list.reverse()

print(octal_list)

multiply_by = 1

new_list = []

for octal in octal_list:
    octal = int(octal)

    result = octal * multiply_by
    new_list.append(result)

    multiply_by = multiply_by * 8

print(new_list)

sum = 0
for value in new_list:
    sum += value

decimal_value = sum
print(f"The decimal value of {input_value} is {decimal_value}\n")

print("*---*---*--- Octal to Decimal Conversion ---*---*---*")
