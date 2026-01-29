def int_to_roman(number_to_convert: int) -> str:
    roman_accumulator: str = ""
    counter: int = number_to_convert

    while counter > 0:
        if counter >= 10:
            roman_accumulator += "X"
            counter -= 10

        if counter >= 5:
            roman_accumulator += "V"
            counter -= 5

        if counter >= 1:
            roman_accumulator += "I"
            counter -= 1

    return roman_accumulator
