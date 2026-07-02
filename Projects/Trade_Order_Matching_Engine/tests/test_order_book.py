from backend.engine.order_book import OrderBook
from backend.engine.order import Order

def test_add_orders():
    book = OrderBook()

    order1 = Order("BUY", 100, 1)
    order2 = Order("BUY", 105, 1)

    book.add_order(order1)
    book.add_order(order2)

    assert len(book.bids) == 2
    assert book.get_best_bid().price == 105

# Test to add buy order

def test_sell_order():
    book = OrderBook()

    order1 = Order("SELL", 100, 1)
    order2 = Order("SELL", 105, 1)

    book.add_order(order1)
    book.add_order(order2)

    assert len(book.asks) == 2
    assert book.get_best_ask().price == 100

# Test to add sell order

def test_bid_display():
    book = OrderBook()

    book.add_order(Order("BUY", 100, 1))
    book.add_order(Order("BUY", 110, 1))
    book.add_order(Order("BUY", 105, 1))

    assert book.get_best_bid().price == 110

# Test for correct bid priority

def test_ask_display():
    book = OrderBook()

    book.add_order(Order("SELL", 100, 1))
    book.add_order(Order("SELL", 110, 1))
    book.add_order(Order("SELL", 105, 1))

    assert book.get_best_ask().price == 100

# Test for correct ask priority

def test_remove_best_bid():
    book = OrderBook()

    book.add_order(Order("BUY", 100, 1))
    book.add_order(Order("BUY", 110, 1))
    book.add_order(Order("BUY", 105, 1))

    book.remove_best_bid()

    assert book.get_best_bid().price == 105

# Test of removing bid from heap

def test_remove_best_ask():
    book = OrderBook()

    book.add_order(Order("SELL", 100, 1))
    book.add_order(Order("SELL", 110, 1))
    book.add_order(Order("SELL", 105, 1))

    book.remove_best_ask()

    assert book.get_best_ask().price == 105

# Test of removing ask from heap

def test_display_structure():
    book = OrderBook()

    book.add_order(Order("BUY", 100, 1))
    book.add_order(Order("SELL", 110, 2))

    display = book.get_order_book_display()

    assert display["bids"][0]["price"] == 100
    assert display["asks"][0]["price"] == 110

# Test of corect display structure

def test_empty_orderbook():
    book = OrderBook()

    assert book.get_best_bid() is None
    assert book.get_best_ask() is None

# Test of empty orderbook before sent orders