def process_order(order, database, email):
    if not order.items:
        raise ValueError("empty order")

    total = 0
    for item in order.items:
        total += item.price * item.quantity

    if order.customer.is_vip:
        total = total * 0.9

    database.save(order)
    email.send(order.customer.email, "Order confirmed")

    return {"status": "ok", "total": total}
