import random

from PP_Programowanie_obiektowe.Enkapsulacja.shop.order_element import OrderElement
from PP_Programowanie_obiektowe.Enkapsulacja.shop.product import Product


class Order:

    MAX_ELEMENTS = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ELEMENTS:
            order_elements = order_elements[:Order.MAX_ELEMENTS]
        self._order_elements = order_elements
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
            self.total_price = self._calculate_total_price()
        else:
            print("Osiągnięto limit pozycji w zamówieniu")

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

    def __len__(self):
        return len(self._order_elements)

    @classmethod
    def generate_order(cls, number_of_products):
        number_of_product = number_of_products
        order_elements = []
        for product_number in range(number_of_product):
            product_name = f"Produkt-{product_number}"
            category_name = "Inne"
            unit_price = random.randint(1, 30)
            product = Product(product_name, category_name, unit_price)
            quantity = random.randint(1, 10)
            order_elements.append(OrderElement(product, quantity))

        order = Order(client_first_name="Paweł", client_last_name="Tatar", order_elements=order_elements)
        return order
