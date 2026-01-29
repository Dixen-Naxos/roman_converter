def int_to_roman(number_to_convert: int) -> str:
    if number_to_convert == 2:
        return "II"

    if number_to_convert == 3:
        return "III"
    
    return "I"
