import re
from typing import Any, Dict, List


def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba n nie może być ujemna")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = set("aeiouyAEIOUYąęóĄĘÓ")
    return sum(1 for char in text if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi zawierać się w przedziale 0-1")
    return float(price * (1 - discount))


def flatten_list(nested_list: List[Any]) -> List[Any]:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def word_frequencies(text: str) -> Dict[str, int]:
    if not text:
        return {}
    words = re.findall(r'\b\w+\b', text.lower())
    freq: Dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True