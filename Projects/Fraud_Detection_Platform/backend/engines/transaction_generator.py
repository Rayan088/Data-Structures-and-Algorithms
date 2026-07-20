import random
from datetime import datetime, timedelta

from database.db import db
from models.customer import Customer
from models.transactions import Transaction

# All randomised pools

merchants = {
    "Standard": [
        "Tesco", "ASDA", "McDonalds", "Starbucks", "Amazon",
        "Ebay", "Uber", "Deliveroo", "Shell", "H&M", "T.J.Maxx", "Home Bargains",
        "Sainsbury's", "Aldi", "Lidl", "Costa Coffee", "Subway",
        "KFC", "Burger King", "Morrisons", "Primark", "Boots"
    ],

    "Premium": [
        "Amazon", "Apple", "British Airways", "Hilton Hotels", "Booking.com",
        "Uber", "Selfridges", "John Lewis", "Emirates",
        "Harrods", "The Ritz London", "Rolex", "Tesla", "Louis Vuitton",
        "Gucci", "Burberry", "Singapore Airlines",
        "Four Seasons Hotels", "Bang & Olufsen"
    ],

    "Business": [
        "AWS", "Microsoft Azure", "Salesforce", "Dell", "British Airways",
        "Emirates", "Qatar Airways", "MailChimp", "Adobe", "Zoom", "Office Depot",
        "Google Cloud", "Oracle", "Slack", "Dropbox Business", "HubSpot",
        "Cisco", "Atlassian", "SAP", "Workday", "Notion", "IBM"
    ]
}

devices = [
    "iPhone 17", "iPhone 16", "iPhone 15", "iPhone 14", "Pixel 9", "Pixel 8", "Galaxy S24",
    "Galaxy S23", "OnePlus 12", "Moto Edge", "iPad", "iPad Pro", "iPad Air", "iPad Mini",
    "MacBook Pro", "MacBook Air", "MacBook", "Surface Pro", "Surface Go", "Chromebook"
]

countries = {
    "United Kingdom": "GBP",
    "United States": "USD",
    "France": "EUR",
    "Germany": "EUR",
    "Spain": "EUR",
    "UAE": "AED",
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

            customer.trusted_devices = ",".join(trusted_devices)
            db.session.commit()

            # Generates 2 trusted devices and adding to Customer table

            self.customer_profiles[customer.customer_id] = {
                "avg_amount": avg_amount,
                "favourite_merchants": favourite_merchants,
                "trusted_devices": trusted_devices
            }

    def generate_time_stamp(self):
        days_ago = random.randint(0, 100)
        hours_ago = random.randint(0, 23)
        minutes_ago = random.randint(0, 59)

        timestamp = (datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago))

        return timestamp
    
    # Method for generating timestamp

    def generate_normal_transaction(self, customer):
        profile = self.customer_profiles[customer.customer_id]
        timestamp = self.generate_time_stamp()

        if random.random() < 0.82:
            merchant = random.choice(profile["favourite_merchants"])
        else:
            merchant = random.choice(merchants[customer.account_type])

        # Generating merchant

        amount = profile["avg_amount"]
        random_chance = random.random()
        if random_chance < 0.85:
            amount *= random.uniform(0.6, 1.4)
        else:
            amount *= random.uniform(1.6, 2.0)
        amount = round(amount, 2)

        # Generating amount

        if random.random() < 0.03:
            foreign = [c for c in countries if c != customer.home_country]
            country = random.choice(foreign)
        else:
            country = customer.home_country

        currency = countries[country]

        # Setting country and corresponding currency

        if random.random() < 0.03:
            device = random.choice(devices)
        else:
            device = random.choice(profile["trusted_devices"])

        # Generating device from chosen customer devices

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
        
        return transaction
    
    # Method for generating normal transaction

    def generate_suspicious_transaction(self, customer):
        profile = self.customer_profiles[customer.customer_id]
        timestamp = self.generate_time_stamp()

        merchant = random.choice(profile["favourite_merchants"])

        amount = profile["avg_amount"]
        random_chance = random.random()
        if random_chance < 0.85:
            amount *= random.uniform(0.6, 1.4)
        else:
            amount *= random.uniform(1.6, 2.0)
        amount = round(amount, 2)

        country = customer.home_country
        currency = countries[country]

        device = random.choice(profile["trusted_devices"])   
        
        fraud_rules = random.sample([
            "new_device", "high_amount", "impossible_travel", "unfamiliar_merchant"
        ], k=1)

        if "new_device" in fraud_rules:
            untrusted_devices = [d for d in devices if d not in profile["trusted_devices"]]
            device = random.choice(untrusted_devices)

        if "high_amount" in fraud_rules:
            if customer.account_type == "Standard":
                multiplier = random.uniform(2.5, 5)
            elif customer.account_type == "Premium":
                multiplier = random.randint(2, 4)
            else:
                multiplier = random.uniform(1.5, 3)
            amount = round(profile["avg_amount"] * multiplier, 2)

        if "impossible_travel" in fraud_rules:
            foreign_countries = [c for c in countries.keys() if c != customer.home_country]
            country = random.choice(foreign_countries)
            currency = countries[country]

        if "unfamiliar_merchant" in fraud_rules:
            if customer.account_type == "Standard":
                unfamiliar_m = merchants["Premium"]
                merchant = random.choice(unfamiliar_m)

            elif customer.account_type == "Premium":
                unfamiliar_m = merchants["Business"]
                merchant = random.choice(unfamiliar_m)
            
            else:
                unfamiliar_m = merchants["Business"]
                merchant = random.choice(unfamiliar_m)

        # Generating fraudulent transactions

        transaction = Transaction(
            customer_id = customer.customer_id,
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

        return transaction

    # Method for generating suspicious transaction

    def generate_fraudulent_transaction(self, customer):
        profile = self.customer_profiles[customer.customer_id]
        timestamp = self.generate_time_stamp()

        merchant = random.choice(profile["favourite_merchants"])

        amount = profile["avg_amount"]
        random_chance = random.random()
        if random_chance < 0.85:
            amount *= random.uniform(0.6, 1.4)
        else:
            amount *= random.uniform(1.6, 2.0)
        amount = round(amount, 2)

        country = customer.home_country
        currency = countries[country]

        device = random.choice(profile["trusted_devices"])

        severity = random.random()
        if severity < 0.8:
            num_rules = random.randint(2, 3)
        else:
            num_rules = random.randint(3, 4)    
        
        fraud_rules = random.sample([
            "new_device", "high_amount", "impossible_travel", "unfamiliar_merchant"
        ], k=num_rules)

        if "new_device" in fraud_rules:
            untrusted_devices = [d for d in devices if d not in profile["trusted_devices"]]
            device = random.choice(untrusted_devices)

        if "high_amount" in fraud_rules:
            if customer.account_type == "Standard":
                multiplier = random.randint(10, 25)
            elif customer.account_type == "Premium":
                multiplier = random.randint(6, 15)
            else:
                multiplier = random.randint(4, 10)
            amount = round(profile["avg_amount"] * multiplier, 2)

        if "impossible_travel" in fraud_rules:
            foreign_countries = [c for c in countries.keys() if c != customer.home_country]
            country = random.choice(foreign_countries)
            currency = countries[country]

        if "unfamiliar_merchant" in fraud_rules:
            if customer.account_type == "Standard":
                unfamiliar_m = merchants["Premium"]
                merchant = random.choice(unfamiliar_m)

            elif customer.account_type == "Premium":
                unfamiliar_m = merchants["Business"]
                merchant = random.choice(unfamiliar_m)
            
            else:
                unfamiliar_m = merchants["Business"]
                merchant = random.choice(unfamiliar_m)

        # Generating fraudulent transactions

        transaction = Transaction(
            customer_id = customer.customer_id,
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

        return transaction
    
    # Method to generate fraudulent transaction

    def generate_transaction(self, customer):

        fraud_chance = random.random()

        if fraud_chance < 0.70:
            return self.generate_normal_transaction(customer)
        elif fraud_chance < 0.85:
            return self.generate_suspicious_transaction(customer)
        else:
            return self.generate_fraudulent_transaction(customer)
        
    # Method to generate transaction type

    def generate_transactions(self):
        customers = Customer.query.all()

        for customer in customers:
            num_transactions = random.randint(40, 70)

            for _ in range(num_transactions):
                transaction = (self.generate_transaction(customer))

                db.session.add(transaction)

        db.session.commit()

     # Generating transactions per customer

    def get_customer_profile(self, customer_id):
        return self.customer_profiles.get(customer_id)

    # Method to get customer profile by id