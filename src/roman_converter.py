def int_to_roman(number_to_convert: int) -> str:
    roman_accumulator: str = ""
    counter: int = number_to_convert

    while counter > 0:
        if counter >= 10:
            roman_accumulator += "X"

        if counter >= 5:
            roman_accumulator += "V"

        roman_accumulator += "I"
        counter -= 1

    return roman_accumulator
