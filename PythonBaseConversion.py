def base_conversion(base10Num, targetBase):
    workingNumber = base10Num
    result = []
    while workingNumber != 0:
        result.insert(0, workingNumber % targetBase)
        workingNumber = int(workingNumber / targetBase)
    print(f"Base 10 input: {base10Num} \n"
          f"Base {targetBase} result: {result}")

def base_conversion_limited(base10Num, targetBase):
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
    while workingNumber != 0:
        hex_converted_result = hex_conversion_dict[workingNumber % targetBase]
        result = hex_converted_result + result
        workingNumber = int(workingNumber / targetBase)
    print(f"Base 10 input: {base10Num} \n"
          f"Base {targetBase} result: {result}")


base_conversion_limited(4600, 13)
