import magazine.utils as utils


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_details(self) -> str:
        formatted_price = utils.format_price(self.price)
        return f"Produkt: {self.name}, Cena: {formatted_price}"