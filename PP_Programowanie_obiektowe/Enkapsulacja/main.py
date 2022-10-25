
from PP_Programowanie_obiektowe.Enkapsulacja.shop.apple import Apple
from PP_Programowanie_obiektowe.Enkapsulacja.shop.potato import Potato
from PP_Programowanie_obiektowe.Enkapsulacja.shop.order import generate_order

def run_homework():

    # green_apple = Apple(species_name="Green", size="M", price=3.5)
    # red_apple = Apple(species_name="Red", size="S", price=2.8)
    # old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    #
    # print(green_apple)
    # print(red_apple)
    # print(old_potato)

    first_order = generate_order()
    print(first_order)

if __name__ == '__main__':
    run_homework()
