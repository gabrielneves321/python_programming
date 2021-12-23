from datetime import datetime
from market_system import Client, Seller, Purchase


def main():
    client = Client('Maria Roberta', 45)
    seller = Seller('Pedro Barros', 36, 5000)
    purchase1 = Purchase(client, datetime.now(), 512)
    purchase2 = Purchase(client, datetime(2018, 6, 4), 256)
    client.register_purchase(purchase1)
    client.register_purchase(purchase2)
    print(f'Client: {client}', '(adult)' if client.is_adult()else'')
    print(f'Seller: {seller}')

    total_value = client.total_purchases()
    Quantity_of_purchases = len(client.purchases)
    print(f'Total: {total_value} em {Quantity_of_purchases} purchases')
    print(f'Last purchase: {client.get_date_last_purchase()}')

if __name__ == '__main__':
    main()