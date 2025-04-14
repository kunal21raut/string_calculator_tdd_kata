
def add(numbers: str) -> int:
    total = 0
    negatives =[]
    delimiter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]

    numbers = numbers.replace("\n", delimiter)

    if numbers:
        for n in numbers.split(delimiter):
            value = int(n)
            if value < 0:
                negatives.append(value)
            total += value

    if negatives:
        negative_str = ", ".join(str(n) for n in negatives)
        raise ValueError(f"negative numbers not allowed: {negative_str}")
    return total


