def greet(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


welcome_message: str = greet("Zuzanna", "Chmielewska")
print(welcome_message)