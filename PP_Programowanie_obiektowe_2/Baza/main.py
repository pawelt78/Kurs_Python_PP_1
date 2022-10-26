
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
    loyal_customer_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
    christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)

    print(normal_order)
    print(loyal_customer_order)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
