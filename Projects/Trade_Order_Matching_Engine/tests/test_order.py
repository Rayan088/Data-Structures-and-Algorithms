from backend.engine.order import Order

def test_order_creation():
    order = Order("BUY", 50000, 0.5)

    assert order.side == "BUY"
    assert order.price == 50000
    assert order.quantity == 0.5
    assert order.filled == 0
    assert order.status == "OPEN"

# Test for correct order generation

def test_id_increment():
    order1 = Order("BUY", 50000, 0.5)
    order2 = Order("SELL", 60000, 0.4)

    assert order1.id == order2.id - 1

# Test for order if incrementation

def test_order_filled():
    order = Order("BUY", 50000, 0.5)
    order.filled = 0.5

    assert order.remaining_quantity() == 0

# Test for complete order fill

def test_partial_order_fill():
    order = Order("BUY", 50000, 0.5)
    order.filled = 0.3

    assert order.remaining_quantity() == 0.2

# Test for partial order fill