from flask import Flask, jsonify
from flask_cors import CORS
import threading

from backend.engine.matching_engine import MatchingEngine
from backend.bots.market_maker import MarketMaker
from backend.market.market_data import get_market_summary

app = Flask(__name__)
CORS(app)

engine = MatchingEngine()
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

if __name__ == "__main__":
    app.run(debug=True)