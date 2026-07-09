from flask import Flask
from config import Config
from database.db import db

from models.customer import Customer
from models.transactions import Transaction
from models.alert import Alert

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "API Running"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)