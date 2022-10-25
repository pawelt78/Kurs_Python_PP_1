
from PP_Programowanie_obiektowe.Enkapsulacja.shop.apple import Apple
from PP_Programowanie_obiektowe.Enkapsulacja.shop.potato import Potato
from PP_Programowanie_obiektowe.Enkapsulacja.shop.order import Order
from PP_Programowanie_obiektowe.Enkapsulacja.shop.product import Product


def run_homework():
    first_order = Order.generate_order(4)
    print(first_order)

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    first_order.add_product_to_order(cookie, quantity=10)
    print(first_order)


if __name__ == '__main__':
    run_homework()
