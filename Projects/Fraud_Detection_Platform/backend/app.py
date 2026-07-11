from flask import Flask
from config import Config
from database.db import db

from models.customer import Customer
from models.transactions import Transaction
from models.alert import Alert

from engines.customer_generator import customerGenerator
from engines.transaction_generator import TransactionGenerator

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "API Running"

if __name__ == "__main__":
    with app.app_context():

        db.drop_all()
        db.create_all()

        customer_generator = customerGenerator()
        customer_generator.generate_customers(250)

        transaction_generator = TransactionGenerator()
        transaction_generator.generate_transactions()

    app.run(debug=True)