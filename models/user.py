class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def get_info(self) -> str:
        return f"Użytkownik: {self.username} ({self.email})"