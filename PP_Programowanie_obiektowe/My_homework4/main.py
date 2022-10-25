
# Podziel projekt - utwórz nowy pakiet (shop) i przenieś do osobnych modułów (plików) w pakiecie shop:
# a. Klasę Apple
# b. Klasę Potato
# c. Klasę Product oraz funkcje generujące i wypisujące produkt
# d. Klasę Order oraz funkcje generujące i wypisujące zamówienie
# e. Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje

from shop.apple import Apple
from shop.order import generate_order
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=1.2)
    red_apple = Apple(species_name="Red", size="S", price=2.8)

    print(f"10kg zielonego jabłka kosztuje: {green_apple.calculate_price(10)}")
    print(f"10kg czerwonego jabłka kosztuje: {red_apple.calculate_price(5)}")


    # print(green_apple.species_name, green_apple)
    # print(red_apple.species_name, red_apple)

    # old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    # print(old_potato.species_name, old_potato)

    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()



if __name__ == '__main__':
    run_homework()
