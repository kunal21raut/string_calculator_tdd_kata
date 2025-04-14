
def add(numbers: str) -> int:
    total = 0
    negatives =[]
    delimiter = ","

    # check for the number startswith delimiters
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]


    # Replace newline characters with the delimiter to normalize the string
    numbers = numbers.replace("\n", delimiter)

    if numbers:
        number_list = numbers.split(delimiter)
        valid_numbers = []

        for n in number_list:
            if n:  # will skip empty strings
                num = int(n)
                if num < 0:
                    negatives.append(num)
                valid_numbers.append(num)

        if negatives:
            negative_str = ", ".join(str(n) for n in negatives)
            raise ValueError(f"negative numbers not allowed: {negative_str}")
        
        for n in valid_numbers:
                total += n

    return total


