import time
import random

from database.db import db
from models.customer import Customer
from engines.transaction_generator import TransactionGenerator

class LiveTransactionGenerator:
    def __init__(self):
        self.transaction_generator = TransactionGenerator()
        
    def start(self):
        while True:
            customer = random.choice(Customer.query.all())

            transaction = self.transaction_generator.generate_transaction(customer)

            db.session.add(transaction)

            db.session.commit()

            time.sleep(1)

    # Creates one new transaction per second