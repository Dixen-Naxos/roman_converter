import pytest

from src.roman_converter import int_to_roman


class TestRomanConverter:
    @pytest.mark.parametrize("number_to_convert, expected",
                             [[1, "I"], [2, "II"], [3, "III"], [4, "IV"],
                              [5, "V"], [6, "VI"], [7, "VII"],
                              [8, "VIII"], [9, "IX"],[10, "X"], [11, "XI"],
                              [12, "XII"], [13, "XIII"], [15, "XV"],
                              [20, "XX"], [40, "XL"], [60, "LX"], [90, "XC"],[100, "C"],])
    def test_roman_to_int_for_number_one(self, number_to_convert, expected):
        assert int_to_roman(number_to_convert) == expected
