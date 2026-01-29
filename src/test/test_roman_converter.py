import pytest

from src.roman_converter import int_to_roman


class TestRomanConverter:
    @pytest.mark.parametrize("number_to_convert, expected", [[1, "I"], [2, "II"], [3, "III"], [5, "V"]])
    def test_roman_to_int_for_number_one(self, number_to_convert, expected):
        assert int_to_roman(number_to_convert) == expected
