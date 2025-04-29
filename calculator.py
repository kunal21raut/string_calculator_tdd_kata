
def add(numbers: str) -> int:
    total = 0
    negatives =[]
    delimiter = ","

    multiply_total = 1
    star_delimeter = []
    is_multiply = False

    # check for the number startswith delimiters
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]

        if delimiter == "*":
            # numberss = numbers.replace("*", ",")
            is_multiply = True

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
                
                elif num <= 1000:  # only accept numbers <= 1000
                    valid_numbers.append(num)

                elif delimiter == "*":
                    star_delimeter.append(num)

        if negatives:
            negative_str = ", ".join(str(n) for n in negatives)
            raise ValueError(f"negative numbers not allowed: {negative_str}")
        
        if is_multiply:
            for n in valid_numbers: 
                multiply_total = multiply_total * n
            return multiply_total
        else:
            for n in valid_numbers:
                total = total +n


    return total


