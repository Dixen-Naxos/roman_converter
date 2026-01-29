ROMAN_NUMBER_ASSOCIATION: list[list] = [
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
]
def int_to_roman(number_to_convert: int) -> str:
    roman_accumulator: str = ""
    counter: int = number_to_convert


    while counter > 0:
        for roman_number_couple in ROMAN_NUMBER_ASSOCIATION:
            value, symbol = roman_number_couple
            if counter >= value:
                roman_accumulator += symbol
                counter -= value
                break

    return roman_accumulator
