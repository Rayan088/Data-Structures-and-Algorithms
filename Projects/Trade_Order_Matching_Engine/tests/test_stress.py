import time
from backend.engine.matching_engine import MatchingEngine
from backend.account.wallet import Wallet
from backend.engine.order import Order

# Tests capability of matching engine

def test_orders_per_second():
    wallet = Wallet()
    engine = MatchingEngine(wallet)

    num_orders = 10000

    start = time.time()

    for i in range(num_orders):
        order = Order(
            side="BUY" if i % 2 == 0 else "SELL",
            price=50000 + (i % 10),
            quantity=0.1,
            is_user=False
        )

        engine.add_order(order)

    end = time.time()

    duration = end - start
    ops_per_sec = num_orders / duration

    print("\n===== STRESS TEST RESULT =====")
    print(f"Orders processed: {num_orders}")
    print(f"Time taken: {duration:.4f} sec")
    print(f"Throughput: {ops_per_sec:.2f} orders/sec")

    print(f"Trades executed: {len(engine.trades)}")
    print(f"Orders processed/sec: {num_orders/duration:.0f}")
    print(f"Trades/sec: {len(engine.trades)/duration:.0f}")

    assert ops_per_sec > 1000