class Order:
    pass


class Product:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == '__main__':
    apple1 = Apple()
    apple2 = Apple()
    potato1 = Potato()
    potato2 = Potato()

    print("type of potato1:", type(potato1))
    print("type of potato2:", type(potato2))
    print("type of apple1:", type(apple1))
    print("type of apple2:", type(apple2))

    orders = [Order(), Order(), Order(), Order(), Order()]

    products = {
        "jabłko": Product(),
        "gruszka": Product(),
        "ziemniak": Product(),
        "śliwki": Product()

    }
    print(products)
