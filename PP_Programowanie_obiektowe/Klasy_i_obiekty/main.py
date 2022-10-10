import random

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:
    def __init__(self, name_surname, product_list):
        self.name_surname = name_surname

        # if product_list is None:
        #     product_list = []
        self.full_price = None
        for number_of_orders in range(len(product_list)):
            self.full_price += product_list(number_of_orders).price


class Apple:
    def __init__(self, genre, size, price_per_kilogram):
        self.genre = genre
        self.size = size
        self.price_per_kilogram = price_per_kilogram


class Potato:
    def __init__(self, genre, size, price_per_kilogram):
        self.genre = genre
        self.size = size
        self.price_per_kilogram = price_per_kilogram

def create_order(name_of_orderer):
    number_of_products = random.randint(1, 5)
    product_list = []
    for product_number in range(number_of_products):
        name = f"Owoc-{product_number+1}"
        category = "Owoce"
        price = product_number+2
        product_list.append(Product(name, category, price))

    order = Order(name_of_orderer, product_list)
    return order

if __name__ == '__main__':
    jablko1 = Apple(genre="Antonówka", size="L", price_per_kilogram=3)
    jablko2 = Apple(genre="Papierówka", size="M", price_per_kilogram=1)

    potato1 = Potato(genre="Ziemniak wczesny", size="S", price_per_kilogram=5)
    potato2 = Potato(genre="Ziemniak pastewny", size="XL", price_per_kilogram=2)

print(jablko1)
print(jablko2)
print(potato1)
print(potato2)

Nowe_zamowienie = create_order("Paweł Tatar")
print(Nowe_zamowienie)