from .people import People


def get_date(purchase):
    return purchase.date


class Client(People):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.purchase = []

    def register_purchase(self, purchase):
        self.purchases.append(purchase)

    def get_date_last_purchase(self):
        return None if not self.purchase else \
            sorted(self.purchases, key=get_date)[-1].date

    def total_purchases(self):
        total = 0
        for purchase in self.purchases:
            total += purchase.value
        return total
