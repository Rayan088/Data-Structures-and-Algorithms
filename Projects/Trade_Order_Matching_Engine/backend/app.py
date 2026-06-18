from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

from backend.engine.matching_engine import MatchingEngine
from backend.bots.market_maker import MarketMaker
from backend.market.market_data import get_market_summary
from backend.account.wallet import Wallet
from backend.engine.order import Order

app = Flask(__name__)
CORS(app)

wallet = Wallet()
engine = MatchingEngine(wallet)
bot = MarketMaker(engine)

threading.Thread(target=bot.start, daemon=True).start()

@app.route('/orderbook')
def orderbook():
    return jsonify({
        "bids": [{"price": order.price, "qty": order.quantity} for order in engine.order_book.get_bids()],
        "asks": [{"price": order.price, "qty": order.quantity} for order in engine.order_book.get_asks()]
    })

@app.route('/trades')
def trades():
    return jsonify([
        {
            "price": t.price,
            "qty": t.quantity,
            "side": t.side
        }
        for t in engine.trades
    ])

@app.route('/market')
def market():
    return jsonify(get_market_summary())

@app.route('/order', methods=["POST"])
def place_order():
    data = request.json

    side = data["side"]
    price = float(data["price"])
    qty = float(data["quantity"])

    if side == "BUY":
        cost = price * qty
        if not wallet.can_buy(cost):
            return jsonify({"error": "Insufficient USD"}), 400

    if side == "SELL":
        if not wallet.can_sell(qty):
            return jsonify({"error": "Insufficient BTC"}), 400

    order = Order(side, price, qty, is_user=True)

    engine.add_order(order)

    return jsonify({"status": "order placed"})

if __name__ == "__main__":
    app.run(debug=True)