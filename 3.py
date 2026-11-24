print("*---*---*--- Hexadecimal to Decimal Conversion ---*---*---*\n")

input_value = ""

while True:
    input_value = input("Enter a Hexadecimal number to convert: ")

    # check if the input is empty

    if input_value == "":
        print("Enter something please.\n")
        continue

    # make sure the input is only 0 to 9 or A to F

    is_valid = True

    for char in input_value:
        if char not in '0123456789ABCDEFabcdef': # include lowercase
            is_valid = False

    # check if it is still valid

    if is_valid:
        break # stop the while loop
    else:
        print("The inputted value is invalid.\n")

hexa_list = list(input_value)
hexa_list.reverse()
print(hexa_list)

multiply_by = 1
new_list = []

for hexa in hexa_list:
    num = 0
    if hexa.isalpha():
        hexa = hexa.lower()

    if hexa == "a":
        num = 10
    elif hexa == "b":
        num = 11
    elif hexa == "c":
        num = 12
    elif hexa == "d":
        num = 13
    elif hexa == "e":
        num = 14
    elif hexa == "f":
        num = 15
    else:
        num = int(hexa)

    result = num * multiply_by
    new_list.append(result)
    multiply_by = multiply_by * 16

print(new_list)
sum = 0

for value in new_list:
    sum += value

decimal_value = sum
print(f"The decimal value of {input_value} is {decimal_value}\n")

print("---*---*--- Hexadecimal to Decimal Conversion ---*---*---")