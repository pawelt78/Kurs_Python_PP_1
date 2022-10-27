
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


def run_homework():
    first_name = "Paweł"
    last_name = "Tatar"

    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    print(normal_order)

    new_elements = generate_order_elements(3)
    normal_order.order_elements = new_elements
    print(normal_order)

    too_many_elements = generate_order_elements(1000)
    normal_order.order_elements = too_many_elements
    print(normal_order)

    print(normal_order.total_price)


if __name__ == '__main__':
    run_homework()
