import random
from datetime import datetime, timedelta

from database.db import db
from models.customer import Customer
from models.transactions import Transaction

# All randomised pools

merchants = {
    "Standard": [
        "Tesco", "ASDA", "McDonalds", "Starbucks", "Amazon",
        "Netflix", "Uber", "Deliveroo", "Shell",
        "Sainsbury's", "Aldi", "Lidl", "Costa Coffee", "Subway",
        "KFC", "Burger King", "Morrisons", "Primark", "Boots"
    ],

    "Premium": [
        "Amazon", "Apple", "British Airways", "Hilton Hotels", "Booking.com",
        "Uber", "Selfridges", "John Lewis", "Emirates",
        "Harrods", "The Ritz London", "Rolex", "Tesla", "Louis Vuitton",
        "Gucci", "American Express Travel", "Singapore Airlines",
        "Four Seasons Hotels", "Bang & Olufsen"
    ],

    "Business": [
        "AWS", "Microsoft Azure", "Salesforce", "Dell", "British Airways",
        "Adobe", "LinkedIn Premium", "Zoom", "Office Depot",
        "Google Cloud", "Oracle", "Slack", "Dropbox Business", "HubSpot",
        "Cisco", "Atlassian", "SAP", "Workday", "Notion"
    ]
}

devices = [
    "iPhone 17",
    "iPhone 15",
    "Samsung Galaxy S24",
    "Windows Laptop",
    "MacBook Pro",
    "iPad"
]

countries = {
    "United Kingdom": "GBP",
    "United States": "USD",
    "France": "EUR",
    "Germany": "EUR",
    "Spain": "EUR",
    "United Arab Emirates": "AED",
    "Brazil": "BRL"
}

class TransactionGenerator:
    def __init__(self):
        self.customer_profiles = {}
        self.build_profiles()

    # Initializer method

    def build_profiles(self):
        customers = Customer.query.all()

        for customer in customers:
            if customer.account_type == "Standard":
                avg_amount = random.randint(20, 80)
            elif customer.account_type == "Premium":
                avg_amount = random.randint(80, 300)
            else:
                avg_amount = random.randint(200, 1500)

            # Sets account spending based on account type

            favourite_merchants = random.sample(merchants[customer.account_type], k=5)

            # Sets favourite merchants based on account type

            trusted_devices = random.sample(devices, 2)

            # Generates 2 trusted devices

            self.customer_profiles[customer.customer_id] = {
                "avg_amount": avg_amount,
                "favourite_merchants": favourite_merchants,
                "trusted_devices": trusted_devices
            }


    def generate_transaction(self, customer):
        profile = self.customer_profiles[customer.customer_id]

        days_ago = random.randint(0, 365)
        hours_ago = random.randint(0, 23)
        minutes_ago = random.randint(0, 59)

        timestamp = (datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago))

        # Generating timestamp

        account_merchants = merchants[customer.account_type]

        random_merchant = random.random()

        all_merchants = (merchants["Standard"] + merchants["Premium"] + merchants["Business"])

        if random_merchant < 0.7:
            merchant = random.choice(profile["favourite_merchants"])
        elif random_merchant < 0.96:
            merchant = random.choice(account_merchants)
        else:
            merchant = random.choice(all_merchants)

        # Setting merchant

        amount = abs(random.gauss(profile["avg_amount"], profile["avg_amount"] * 0.4))
        amount = round(amount, 2)

        # Setting amount spent

        if random.random() < 0.90:
            country = customer.home_country
            currency = countries[country]
        else:
            country = random.choice(list(countries.keys()))
            currency = countries[country]

        # Setting home country and corresponding currency

        if random.random() < 0.90:
            device = random.choice(profile["trusted_devices"])
        else:
            device = random.choice(devices)

        # Setting devices

        transaction = Transaction(
            customer_id=customer.customer_id,
            timestamp=timestamp,
            merchant=merchant,
            amount=amount,
            country=country,
            currency=currency,
            device=device,
            risk_score=0,
            risk_level="LOW",
            status="PENDING"
            )
        
        # Creating transaction
        
        return transaction

    def generate_transactions(self):
        customers = Customer.query.all()

        for customer in customers:
            num_transactions = random.randint(100, 300)

            for _ in range(num_transactions):
                transaction = (self.generate_transaction(customer))

                db.session.add(transaction)

        db.session.commit()

    # Generating transactions per customer