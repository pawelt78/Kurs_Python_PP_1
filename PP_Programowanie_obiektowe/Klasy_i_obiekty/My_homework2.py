class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price


class Order:
    def __init__(self, client_first_name, client_last_name, products):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


class Apple:

    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


def print_product(product):
    print(f"Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.unit_price}/szt")


def print_order(order):
    print("=" * 60)
    print(f"Zamówienie złożone przez: {order.client_first_name} {order.client_last_name}")
    print(f"O łącznej wartości: {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.products:
        print("\t")#, end="")
        print_product(product)
    print("=" * 60)
    print()


def run_homework():
    cookies = Product(name="Cookies", category_name="Food", unit_price=4)
#   empty_order = Order(name_surname="Paweł Tatar")
    order = Order(client_first_name="Paweł", client_last_name="Tatar", products=[cookies])

#   print(empty_order)
    print_order(order)


if __name__ == '__main__':
    run_homework()
