def contains_element(elements: list, value: int) -> bool:
    return value in elements


numbers_list = [10, 20, 30, 40, 50]
print("Czy lista zawiera 30?", contains_element(numbers_list, 30))
print("Czy lista zawiera 99?", contains_element(numbers_list, 99))