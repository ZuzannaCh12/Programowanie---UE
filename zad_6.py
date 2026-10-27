def process_lists(list1: list, list2: list) -> list:
    unique_elements = set(list1 + list2)
    return [elem ** 3 for elem in unique_elements]


l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print("Wynik przetworzenia list:", process_lists(l1, l2))