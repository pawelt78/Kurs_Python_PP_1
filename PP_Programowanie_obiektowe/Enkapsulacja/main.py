
from PP_Programowanie_obiektowe.Enkapsulacja.shop.apple import Apple
from PP_Programowanie_obiektowe.Enkapsulacja.shop.potato import Potato
from PP_Programowanie_obiektowe.Enkapsulacja.shop.order import Order
from PP_Programowanie_obiektowe.Enkapsulacja.shop.product import Product


# def get_order_price(dupa):
#     return dupa.total_price


def run_homework():
    orders = []
    for _ in range(5):
        orders.append(Order.generate_order(5))

    orders.sort(key=lambda order: order.total_price)

    for order in orders:
        print(order)

if __name__ == '__main__':
    run_homework()
