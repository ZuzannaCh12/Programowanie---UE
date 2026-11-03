import magazine.utils as utils


class Order:
    def __init__(self, order_id: int, total_amount: float):
        self.order_id = order_id
        self.total_amount = total_amount

    def get_summary(self) -> str:
        formatted_total = utils.format_price(self.total_amount)
        return f"Zamówienie #{self.order_id}, Suma: {formatted_total}"