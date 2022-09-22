from PP_niezbednik_adepta.rozne_sposoby_importowania.shop.products_store import update_product_quantity, products

orders = [
    {
        "product": "chleb",
        "quantity": 10,
        "total_price": 35
    }
]


def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Nie mamy tyle towaru!")
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_product_quantity(product_name, quantity)
    orders.append(new_order)
    return new_order
