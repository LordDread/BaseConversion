def base_conversion(base10Num, targetBase):
    hex_conversion_dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    workingNumber = base10Num
    result = ""
    if workingNumber == 0:
        result = "0"
    while workingNumber != 0:
        hex_converted_result = hex_conversion_dict[workingNumber % targetBase]
        result = hex_converted_result + result
        workingNumber = int(workingNumber / targetBase)
    print(f"Base 10 input: {base10Num} \n"
          f"Base {targetBase} result: {result}")

userNumInput = input("Input a non-negative base 10 number: ")
while not (userNumInput.isdigit()) or int(userNumInput) < 0:
    userNumInput = input("Please input a non-negative number: ")

userBaseInput = input("Input a base to convert to (2-16): ")
while not (userBaseInput.isdigit()) or int(userBaseInput) < 2 or int(userBaseInput) > 16:
    userBaseInput = input("Please input a number between 2 and 16: ")

base_conversion(int(userNumInput), int(userBaseInput))
