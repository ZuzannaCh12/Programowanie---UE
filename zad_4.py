def print_every_second_element(numbers) -> None:
    # Wycinek [::2] pobiera co drugi element z listy/zakresu
    for num in numbers[::2]:
        print(num)


# Wywołanie z wykorzystaniem funkcji range(10)
print_every_second_element(list(range(10)))