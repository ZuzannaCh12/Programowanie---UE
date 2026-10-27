def is_even(number: int) -> bool:
    return number % 2 == 0


check_num: int = 8
is_num_even: bool = is_even(check_num)

if is_num_even:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")