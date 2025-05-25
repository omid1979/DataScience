


import random
import datetime
from faker import Faker
import pandas as pd

faker = Faker('fa_IR')
start_date = datetime.datetime(1404, 7, 1)
end_date = datetime.datetime(1404, 9, 30)

# تولید شماره کارت‌ها
cards = [f"6274{random.randint(100000000000, 999999999999)}" for _ in range(900000)]

# تولید تراکنش‌ها
transactions = []
for _ in range(1000000):
    card = random.choice(cards)
    date = faker.date_time_between(start_date, end_date).strftime("%Y/%m/%d %H:%M:%S")
    amount = random.randint(10000, 10000000)
    merchant = f"M{random.randint(100000, 999999)}"
    trans_type = random.choices(["POS", "Online", "ATM"], weights=[0.6, 0.3, 0.1])[0]
    
    transactions.append({
        "card_number": card,
        "transaction_date": date,
        "amount": amount,
        "merchant_id": merchant,
        "transaction_type": trans_type
    })

# ذخیره در فایل CSV
df = pd.DataFrame(transactions)
df.to_csv("transactions.csv", index=False)

