class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return (f"Dom na ul. {self.address} | Powierzchnia: {self.area}m2, Pokoje: {self.rooms}, "
                f"Cena: {self.price} PLN, Działka: {self.plot}m2")


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return (f"Mieszkanie na ul. {self.address} | Powierzchnia: {self.area}m2, Pokoje: {self.rooms}, "
                f"Cena: {self.price} PLN, Piętro: {self.floor}")


# Utworzenie i wyświetlenie obiektów
house = House(180.5, 5, 850000.0, "Słoneczna 15, Katowice", 600)
flat = Flat(54.0, 2, 420000.0, "Korfantego 8, Katowice", 3)

print(house)
print(flat)