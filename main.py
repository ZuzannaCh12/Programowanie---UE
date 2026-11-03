import magazine.Product as Product
from models.user import User


def run() -> None:
    prod = Product.Product("Laptop", 3500.0)
    print(prod.get_details())

    user = User("zuzanna", "zuzanna@example.com")
    print(user.get_info())


if __name__ == "__main__":
    run()