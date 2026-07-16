import time
import random

from database.db import db
from models.customer import Customer

class LiveTransactionGenerator:
    def __init__(self, app, transaction_generator, fraud_engine):
        self.app = app
        self.transaction_generator = transaction_generator
        self.fraud_engine = fraud_engine
        
    def start(self):
        with self.app.app_context():
            customers = Customer.query.all()
            
            while True:
                customer = random.choice(customers)

                transaction = self.transaction_generator.generate_transaction(customer)

                db.session.add(transaction)
                db.session.commit()

                self.fraud_engine.analyse_transaction(transaction, customer)

                db.session.commit()

                time.sleep(1)

    # Creates one new transaction per second