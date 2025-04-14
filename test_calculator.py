from calculator import add

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





