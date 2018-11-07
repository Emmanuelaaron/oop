
pending_orders = [4, 5, 6, 8]
delivered_orders = [1, 2, 32, 100]
user = {"name": "Emma", "password": "emanuel" }

def check_order_status(order_id):
    return(order_id in delivered_orders)

def if_integer(order_id):
    return(type(order_id) is int)

def not_delivered_yet(order_id):
    return (order_id  in pending_orders)

def order_validation(order_id):
    all_orders = pending_orders + delivered_orders
    return (order_id not in all_orders)

def added_to_the_list():
    all_orders = pending_orders + delivered_orders
    return(len(all_orders) > 0)

def add_new_order_to_list(order_id):
    pending_orders.append(order_id)
    return ("Added new order to the list")

def order_delivered(order_id):
    pending_orders.remove(order_id)
    delivered_orders.append(order_id)
    return ("order delivered sucessfully")
