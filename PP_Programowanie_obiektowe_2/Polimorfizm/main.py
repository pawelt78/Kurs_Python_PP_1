
# Dodaj do programu obsługę polityki rabatowej.
# Zaimplementuj funkcje reprezentujące politykę podatkową i przekaż je do konstruktora zamówienia.
# Jeżeli polityka została przekazana to podczas liczenia łącznej kwoty zamówienia należy naliczyć rabat.
# Jeżeli nie - obliczamy łączną kwotę jak dotychczas.
# Zaimplementuj dwie polityki rabatowe:
# Dla stałych klientów: 5% rabatu na każdą pozycję
# Rabat świąteczny: rabat 20 PLN dla zamówień o łącznej kwocie powyżej 100 PLN

from shop.discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from PP_Programowanie_obiektowe_2.Baza.shop.data_generator import generate_order_elements
from PP_Programowanie_obiektowe_2.Dziedziczenie.shop.product import ExpiringProduct
from PP_Programowanie_obiektowe_2.Dziedziczenie.shop.express_order import ExpressOrder


def run_homework():

    order_elements = generate_order_elements()
    ten_percent_discount = PercentageDiscount(discount_percentage=10)
    hundred_pln_discount = AbsoluteDiscount(discount_value=100)

    no_discount_order = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements,
    )
    order_with_percentage_discount = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements,
        discount_policy=ten_percent_discount,
    )
    order_with_absolute_value_discount = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements,
        discount_policy=hundred_pln_discount,
    )

    express_order1 = ExpressOrder(
        delivery_date="10-11-2022",
        client_first_name="Paweł",
        client_last_name="Tatar",
        order_elements=order_elements,
    )

    print(no_discount_order)
    print(order_with_percentage_discount)
    print(order_with_absolute_value_discount)

    print(express_order1)

if __name__ == '__main__':
    run_homework()
