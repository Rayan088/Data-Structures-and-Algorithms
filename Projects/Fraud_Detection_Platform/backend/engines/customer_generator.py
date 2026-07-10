import random
from faker import Faker

from database.db import db
from models.customer import Customer

fake = Faker()

# Data pools with corresponding generation weightings

account_types = ["Standard", "Premium", "Business"]
account_weights = [75, 20, 5]

countries = ["United Kingdom", "United States", "France", "Germany", "Spain", "United Arab Emirates", "Brazil"]
country_weights = [75, 8, 5, 4, 3, 3, 2]

status = ["Active", "Frozen"]
status_weights = [95, 5]

class customerGenerator:
    def generate_customer(self):
        customer = Customer(name=fake.name(),
                            account_type=random.choices(account_types, weights=account_weights)[0],
                            account_status=random.choices(status, weights=status_weights)[0],
                            home_country=random.choices(countries, weights=country_weights)[0]
                            )
        
        return customer
    
    # Method to generate customer identity
        
    def generate_customers(self, count=250):
        for _ in range(count):
            customer = (self.generate_customer())

            db.session.add(customer)

        db.session.commit()

    # Method to generate customer database