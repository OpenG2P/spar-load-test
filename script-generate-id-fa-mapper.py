import csv
from faker import Faker
import random

fake = Faker()

def generate_random_data():
    national_id = fake.random_int(min=1000000000, max=9999999999)
    account_number = fake.random_int(min=1000000000, max=9999999999)
    name = fake.name()
    phone = fake.phone_number()

    return national_id, account_number, name, phone
data = [generate_random_data() for _ in range(1000)]
csv_file_path = "sample_data.csv"
with open(csv_file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["National ID", "Account number", "Name", "Phone"])
    csv_writer.writerows(data)

print(f"CSV file with 1000 rows created: {csv_file_path}")
