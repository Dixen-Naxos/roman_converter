def int_to_roman(number_to_convert: int) -> str:
    roman_accumulator: str = ""
    for i in range(1, number_to_convert + 1):
        roman_accumulator += "I"
        if i % 5 == 0:
            print(roman_accumulator)
            roman_accumulator = roman_accumulator.replace("IIIII", "V")

        if i % 10 == 0:
            print(roman_accumulator)
            roman_accumulator = roman_accumulator.replace("VV", "X")
    return roman_accumulator
