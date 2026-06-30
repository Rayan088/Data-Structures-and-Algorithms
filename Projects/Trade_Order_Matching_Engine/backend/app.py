from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

import os
from dotenv import load_dotenv
load_dotenv()

from backend.engine.matching_engine import MatchingEngine
from backend.bots.market_maker import MarketMaker
from backend.market.market_data import get_market_summary
from backend.market.market_stats import calculate_market_stats
from backend.account.wallet import Wallet
from backend.engine.order import Order
from backend.database.db import db

from backend.database.models import Wallet as WalletModel

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

wallet = Wallet()
engine = MatchingEngine(wallet)
bot = MarketMaker(engine)

threading.Thread(target=bot.start, daemon=True).start() # Starts bot in background

@app.route('/orderbook')
def orderbook():
    return jsonify({
        "bids": [{"price": order.price, "qty": order.quantity} for order in engine.order_book.bid_display],
        "asks": [{"price": order.price, "qty": order.quantity} for order in engine.order_book.ask_display]
    })

# Data for bids and asks 

@app.route('/trades')
def trades():
    return jsonify([
        {
            "time": t.time,
            "price": t.price,
            "qty": t.quantity,
            "side": t.taker_side
        }
        for t in engine.trades
    ])

# Data for successful trades

@app.route('/market')
def market():
    return jsonify(get_market_summary())

# Data for current market stats

@app.route('/stats')
def stats():
    return jsonify(calculate_market_stats(engine.order_book))

# Mean and spread of current bids and asks

@app.route('/wallet')
def get_wallet():
    w = WalletModel.query.filter_by(user_id=1).first()

    return jsonify({
        "btc": wallet.btc,
        "usd": wallet.cash
    })

# Data of current user wallet

@app.route('/userorders')
def user_orders():
     return jsonify([
        {
            "id": o.id,
            "time": o.time,
            "side": o.side,
            "price": o.price,
            "qty": o.quantity,
            "filled": o.filled,
            "status": o.status
        }
        for o in engine.user_orders
    ])

# Data of current user orders

@app.route('/order', methods=["POST"])
def place_order():
    try:
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

    except Exception as e:
        print(f"Order error: {e}")
        return jsonify({"error": str(e)}), 500

# Method for trade execution

if __name__ == "__main__":
    with app.app_context():

        db.create_all()

        if not WalletModel.query.first():

            wallet = WalletModel(
                user_id=1,
                btc_balance=0,
                usd_balance=10000
            )

            db.session.add(wallet)
            db.session.commit()

            print("Wallet created")

    app.run(debug=True)