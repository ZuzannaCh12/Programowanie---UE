import requests


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: str, country: str):
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.city: str = city
        self.state: str = state
        self.country: str = country

    def __str__(self) -> str:
        return f"Browar: {self.name} | Typ: {self.brewery_type} | Miasto: {self.city} ({self.country})"


def main():
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        breweries = []

        for item in data:
            brewery = Brewery(
                id=item.get("id", ""),
                name=item.get("name", ""),
                brewery_type=item.get("brewery_type", ""),
                city=item.get("city", ""),
                state=item.get("state", ""),
                country=item.get("country", "")
            )
            breweries.append(brewery)

        for b in breweries:
            print(b)
    else:
        print("Błąd podczas pobierania danych z API")


if __name__ == "__main__":
    main()