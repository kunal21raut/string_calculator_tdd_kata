
def add(numbers: str) -> int:
    total = 0
    
    delimiter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]

    numbers = numbers.replace("\n", delimiter)
    
    if numbers:
        for n in numbers.split(","):
            total += int(n)
    return total


