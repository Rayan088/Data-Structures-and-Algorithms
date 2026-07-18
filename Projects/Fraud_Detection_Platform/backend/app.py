from flask import Flask
from flask_cors import CORS
from config import Config
import threading

from database.db import db

from models.customer import Customer
from models.transactions import Transaction
from models.alert import Alert

from engines.customer_generator import customerGenerator
from engines.transaction_generator import TransactionGenerator
from engines.fraud_detection_engine import FraudDetectionEngine
from engines.live_transaction_generator import LiveTransactionGenerator

from routes.transaction_routes import transaction_bp
from routes.analytics_routes import analytics_bp
from routes.customer_details_routes import customer_details

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(transaction_bp)
app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
app.register_blueprint(customer_details)

@app.route("/")
def home():
    return "API Running"

if __name__ == "__main__":
    with app.app_context():

        print("Creating database...")

        db.drop_all()
        db.create_all()

        print("Generating customers...")

        customer_generator = customerGenerator()
        customer_generator.generate_customers(100)

        print("Generating transactions...")

        transaction_generator = TransactionGenerator()
        transaction_generator.generate_transactions()

        print("Starting fraud analysis...")

        fraud_engine = FraudDetectionEngine(transaction_generator)
        fraud_engine.process_all_transactions()

        live_generator = LiveTransactionGenerator(app, transaction_generator, fraud_engine)
        thread = threading.Thread(target=live_generator.start, daemon=True)
        thread.start()

        db.session.commit()

    app.run(debug=True, use_reloader=False)