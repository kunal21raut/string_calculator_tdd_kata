
def add(numbers: str) -> int:
    total = 0
    if numbers:
        for n in numbers.split(","):
            total += int(n)
    return total
