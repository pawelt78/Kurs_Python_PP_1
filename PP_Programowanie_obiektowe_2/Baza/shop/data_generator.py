from PP_Programowanie_obiektowe_2.Baza.shop.order_element import OrderElement
from PP_Programowanie_obiektowe_2.Baza.shop.product import Product
from PP_Programowanie_obiektowe_2.Baza.shop.order import Order
import random

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_QUANTITY = 1
MAX_QUANTITY = 10


def generate_order_elements(number_of_elements=None):
    order_elements = []
    if number_of_elements is None:
        number_of_elements = random.randint(1, Order.MAX_ELEMENTS)
    for product_number in range(number_of_elements):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
