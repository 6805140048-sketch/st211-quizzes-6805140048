import pytest
from Roman_Numerals2 import roman_numeral

def test_four():
    r = roman_numeral()

    assert r.convert("I") == 1
    assert r.convert("LXVII") == 65
    assert r.convert("MMMCMXCIX") == 3999

def test_invalid():
    r = roman_numeral()

    with pytest.raises(ValueError):         # tests ValueError without stopping
        r.convert("ABCD")                   # tells pytest that you're expecting ValueError

    with pytest.raises(ValueError):
        r.convert("IIII")