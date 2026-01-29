from src.roman_converter import int_to_roman
class TestRomanConverter:
    def test_roman_to_int_for_number_one(self):
        assert int_to_roman(1) == "I"


