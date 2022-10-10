class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


class Order:
    def __init__(self, name_surname, products):
        self.name_surname = name_surname

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


def run_homework():
    jablko1 = Apple(species_name="Antonówka", size="L", price=3)
    jablko2 = Apple(species_name="Papierówka", size="M", price=1)
    print(jablko1.species_name, jablko1)
    print(jablko2.species_name, jablko2)

    potato1 = Potato(species_name="Ziemniak wczesny", size="S", price=5)
    potato2 = Potato(species_name="Ziemniak pastewny", size="XL", price=2)
    print(potato1.species_name, potato1)
    print(potato2.species_name, potato2)

    cookies = Product(name="Cookies", category="Food", unit_price=4)
    #empty_order = Order(name_surname="Paweł Tatar")
    order = Order(name_surname="Paweł Tatar", products=[cookies])
    #print(empty_order)
    print(order)


if __name__ == '__main__':
    run_homework()
