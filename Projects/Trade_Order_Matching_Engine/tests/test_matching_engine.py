from backend.engine.matching_engine import MatchingEngine
from backend.engine.order import Order
from backend.account.wallet import Wallet

def setup_engine():
    wallet = Wallet()
    engine = MatchingEngine(wallet)

    return engine, wallet

# Helper function

def test_no_match():
    engine, wallet = setup_engine()

    buy = Order("BUY", 100, 1)
    sell = Order("SELL", 110, 1)

    engine.add_order(buy)
    engine.add_order(sell)

    assert len(engine.trades) == 0
    assert buy.filled == 0
    assert sell.filled == 0

# Test for no orders matching

def test_simple_match():
    engine, wallet = setup_engine()

    buy = Order("BUY", 100, 1)
    sell = Order("SELL", 100, 1)

    engine.add_order(buy)
    engine.add_order(sell)

    assert len(engine.trades) == 1
    assert buy.filled == 1
    assert sell.filled == 1
    assert buy.status == "CLOSED"
    assert sell.status == "CLOSED"

# Test for simple match with full trade executed

def test_partial_fill():
    engine, wallet = setup_engine()

    buy = Order("BUY", 100, 2)
    sell = Order("SELL", 100, 1)

    engine.add_order(buy)
    engine.add_order(sell)

    assert len(engine.trades) == 1
    assert buy.filled == 1
    assert sell.filled == 1
    assert buy.status == "OPEN"
    assert sell.status == "CLOSED"

# Test for partial fill

def test_multiple_fills():
    engine, wallet = setup_engine()

    buy = Order("BUY", 100, 3)
    sell1 = Order("SELL", 100, 1)
    sell2 = Order("SELL", 100, 2)

    engine.add_order(buy)
    engine.add_order(sell1)
    engine.add_order(sell2)

    assert len(engine.trades) == 2
    assert buy.filled == 3
    assert buy.status == "CLOSED"

# Test for same buy order filled by multiple sell orders

def test_wallet_updates_buy_side():
    engine, wallet = setup_engine()

    wallet.btc = 0
    wallet.cash = 1000
    
    buy = Order("BUY", 100, 2, is_user=True) # User order
    sell = Order("SELL", 100, 2) # Bot order

    engine.add_order(buy)
    engine.add_order(sell)

    assert wallet.btc == 2
    assert wallet.cash == 800

# Test wallet correctly updates on bids

def test_wallet_updates_sell_side():
    engine, wallet = setup_engine()

    wallet.btc = 5
    wallet.cash = 1000
    
    buy = Order("BUY", 100, 2) # Bot order
    sell = Order("SELL", 100, 2, is_user=True) # User order

    engine.add_order(buy)
    engine.add_order(sell)

    assert wallet.btc == 3
    assert wallet.cash == 1200

# Tests wallet correctly updates on sells

def test_price_priority_match():
    engine, wallet = setup_engine()

    buy = Order("BUY", 110, 1)
    sell = Order("SELL", 100, 1)

    engine.add_order(buy)
    engine.add_order(sell)

    assert engine.trades[0].price == 100

# Test for trade executed at sell price