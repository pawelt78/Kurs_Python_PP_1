
# Dodaj do programu obsługę polityki rabatowej.
# Zaimplementuj funkcje reprezentujące politykę podatkową i przekaż je do konstruktora zamówienia.
# Jeżeli polityka została przekazana to podczas liczenia łącznej kwoty zamówienia należy naliczyć rabat.
# Jeżeli nie - obliczamy łączną kwotę jak dotychczas.
# Zaimplementuj dwie polityki rabatowe:
# Dla stałych klientów: 5% rabatu na każdą pozycję
# Rabat świąteczny: rabat 20 PLN dla zamówień o łącznej kwocie powyżej 100 PLN

from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.order import Order
from PP_Programowanie_obiektowe_2.Baza.shop.data_generator import generate_order_elements
from PP_Programowanie_obiektowe_2.Dziedziczenie.shop.product import ExpiringProduct
from PP_Programowanie_obiektowe_2.Dziedziczenie.shop.express_order import ExpressOrder


def run_homework():

    order_elements = generate_order_elements()
    first_order = ExpressOrder(
        delivery_date="10-11-2022",
        client_first_name="Paweł",
        client_last_name="Tatar",
        order_elements=order_elements)
    print(first_order)


if __name__ == '__main__':
    run_homework()
