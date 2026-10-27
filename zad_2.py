# V1: Z wykorzystaniem pętli for
def multiply_by_two_loop(numbers: list) -> list:
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


# V2: Z wykorzystaniem listy składanej (list comprehension)
def multiply_by_two_comprehension(numbers: list) -> list:
    return [num * 2 for num in numbers]


# Testowanie funkcji
liczniki = [1, 3, 5, 7, 9]

print("Wynik pętli for:", multiply_by_two_loop(liczniki))
print("Wynik listy składanej:", multiply_by_two_comprehension(liczniki))