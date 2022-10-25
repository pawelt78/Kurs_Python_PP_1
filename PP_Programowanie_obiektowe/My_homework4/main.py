
# Podziel projekt - utwórz nowy pakiet (shop) i przenieś do osobnych modułów (plików) w pakiecie shop:
# a. Klasę Apple
# b. Klasę Potato
# c. Klasę Product oraz funkcje generujące i wypisujące produkt
# d. Klasę Order oraz funkcje generujące i wypisujące zamówienie
# e. Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje

from shop.apple import Apple
from shop.order import generate_order
from shop.potato import Potato

from PP_Programowanie_obiektowe.My_homework4.shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product



def run_homework():
    # first_order = generate_order()
    # print(first_order)
    # second_order = generate_order()
    # print(second_order)


    # green_apple = Apple(species_name="Green", size="M", price=3.5)
    # red_apple = Apple(species_name="Red", size="S", price=2.8)
    # old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    #
    # print(green_apple)
    # print(red_apple)
    # print(old_potato)

    # first_order = generate_order()
    # print(first_order)
    # print(f"Liczba elementów w zamówieniu: {len(first_order)}")
    # second_order = generate_order()
    # print(second_order)
    # print(f"Liczba elementów w zamówieniu: {len(second_order)}")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#homework 4
    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    # other_cookie = Product(name="Inne ciastko", category_name="Jedzenie", unit_price=4)
    juice = Product(name="Sok", category_name="Napoje", unit_price=3)
    first_order_elements = [
        OrderElement(product=cookie, quantity=3),
        # OrderElement(product=other_cookie, quantity=3),
        OrderElement(product=juice, quantity=4),
    ]
    # first_order_elements.append(OrderElement(product=juice, quantity=4))
    # first_order_elements[0].quantity = 10

    second_order_elements = [
        OrderElement(product=juice, quantity=4),
        OrderElement(product=cookie, quantity=3),
    ]

    first_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=first_order_elements)
    second_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=second_order_elements)
    # second_order.client_last_name = "Lewandowski"

    if first_order == second_order:
        print("Te zamówienia są takie same!")
    else:
        print("Te zamówienia są różne!")


if __name__ == '__main__':
    run_homework()

