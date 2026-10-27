def check_sum(a: int, b: int, c: int) -> bool:
    return (a + b) >= c


result: bool = check_sum(5, 4, 8)
print("Suma 2 pierwszych >= trzeciej:", result)