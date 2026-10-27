def print_even_numbers(numbers) -> None:
    for num in numbers:
        if num % 2 == 0:
            print(num)


# Wywołanie z wykorzystaniem funkcji range(10)
print_even_numbers(range(10))