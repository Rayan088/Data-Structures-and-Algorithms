from backend.account.wallet import Wallet

def test_wallet_state():
    wallet = Wallet()

    assert wallet.btc == 1.0
    assert wallet.cash == 0.0

# Test for initial wallet state

def test_can_buy_true():
    wallet = Wallet()
    wallet.cash = 1000

    assert wallet.can_buy(500) is True

# Test for approved transaction

def test_can_buy_false():
    wallet = Wallet()
    wallet.cash = 100

    assert wallet.can_buy(500) is False

# Test for declined transaction

def test_can_sell_true():
    wallet = Wallet()
    
    assert wallet.can_sell(0.3) is True

# Test for approved wallet sale

def test_can_sell_false():
    wallet = Wallet()
    wallet.btc = 0.5

    assert wallet.can_sell(0.7) is False

# Test for declined wallet sale

def test_buy_btc_success():
    wallet = Wallet()
    wallet.cash = 100000

    result = wallet.buy_btc(10000, 2)

    assert result is True
    assert wallet.cash == 80000
    assert wallet.btc == 3.0

# Test for successful btc purchase

def test_buy_btc_fail():
    wallet = Wallet()
    wallet.cash = 100

    result = wallet.buy_btc(10000, 2)

    assert result is False
    assert wallet.cash == 100
    assert wallet.btc == 1.0

# Test for failed btc purchase

def test_sell_btc_success():
    wallet = Wallet()
    
    result = wallet.sell_btc(50000, 0.5)

    assert result is True
    assert wallet.btc == 0.5
    assert wallet.cash == 25000

# Test for successful btc sale

def test_sell_btc_fail():
    wallet = Wallet()

    result = wallet.sell_btc(50000, 1.5)

    assert result is False
    assert wallet.btc == 1.0
    assert wallet.cash == 0.0

# Test for failed btc sale

def test_total_value():
    wallet = Wallet()
    wallet.cash = 100000
    
    total = wallet.get_total_value(50000)

    assert total == 150000

# Test for correct total portfolio value