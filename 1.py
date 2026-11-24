print("*---*---*--- Binary to Decimal Conversion ---*---*---*\n")

input_value = ""

while True:
    input_value = input("Enter a Binary number to convert: ")

    # check if the input is empty

    if input_value == "":
        print("Enter something please.\n")
        continue

    # make sure the input is only 0's and 1's

    is_valid = True

    for char in input_value:
        if char != '0' and char != '1':
            is_valid = False

    # check if it is still valid

    if is_valid:
        break # stop the while loop
    else:
        print("The inputted value is invalid.\n")
        
# convert input_value to list
binary_list = list(input_value)
binary_list.reverse()

print(binary_list)

multiply_by = 1

new_list = []

for binary in binary_list:
    binary = int(binary)

    result = binary * multiply_by
    new_list.append(result)

    multiply_by = multiply_by + multiply_by

print(new_list)

sum = 0
for value in new_list:
    sum += value

decimal_value = sum
print(f"The decimal value of {input_value} is {decimal_value}\n")

print("*---*---*--- Binary to Decimal Conversion ---*---*---*")
