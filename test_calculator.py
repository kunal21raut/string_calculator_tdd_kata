from calculator import add
import pytest

#Empty string returns 0
def test_empty_string_returns_0():
    assert add("") == 0

# One number returns the number
def test_single_number():
    assert add("5") == 5

# Two comma-separated numbers
def test_two_numbers():
    assert add("1,9") == 10

#Handle any amount of numbers
def test_multiple_numbers():
    assert add("192,3,5") == 200



# Allow newline \n as a delimiter 
def test_newline_as_delimiter():
    assert add("1\n2,3") == 6

# Support different delimiters like //;\n1;2
def test_custom_delimiter():
    assert add("//;\n1;2") == 3

# Support different delimiters like //*\n1*2
def test_custom_delimiter_star():
    assert add("//*\n2*5") == 10

#Throw exception for negative numbers

def test_negative_number_raises_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        add("1,-1")

def test_multiple_negatives_raise_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1, -2"):
        add("1,-1,-2")

# ignoring the numbers greater than 1000
def test_ignore_numbers_greater_than_1000():
    assert add("2,1001") == 2
