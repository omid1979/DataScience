import random
import datetime
import pandas as pd

# تنظیم بازه زمانی (۱ مهر ۱۴۰۴ تا ۳۰ آذر ۱۴۰۴)
start_date = datetime.datetime(1404, 7, 1)
end_date = datetime.datetime(1404, 9, 30)

# تولید ۹۰۰,۰۰۰ شماره کارت منحصربه‌فرد
prefixes = ["6274", "5892", "5022", "6104", "6037"]  # پیشوندهای بانکی ایرانی
cards = [random.choice(prefixes) + str(random.randint(100000000000, 999999999999)) for _ in range(900000)]

# تولید ۱,۰۰۰,۰۰۰ تراکنش
transactions = []
for _ in range(1000000):
    card = random.choice(cards)
    # تولید تاریخ و زمان تصادفی
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    transaction_date = (start_date + datetime.timedelta(seconds=random_seconds)).strftime("%Y/%m/%d %H:%M:%S")
    # تولید مبلغ تصادفی
    amount = random.randint(10000, 100000000)
    amount = round(amount / 10000) * 1000  # رُند کردن به مضرب ۱,۰۰۰

    # تولید کد پذیرنده
    merchant_id = f"M{random.randint(100000000, 999999999)}"
    # انتخاب نوع تراکنش با توزیع مشخص
    transaction_type = random.choices(["POS", "Online", "ATM"], weights=[0.6, 0.3, 0.1])[0]
    
    transactions.append({
        "card_number": card,
        "transaction_date": transaction_date,
        "amount": amount,
        "merchant_id": merchant_id,
        "transaction_type": transaction_type
    })

# ذخیره داده‌ها در فایل CSV
df = pd.DataFrame(transactions)
df.to_csv("transactions.csv", index=False, encoding="utf-8")
print("فایل transactions.csv با موفقیت تولید شد.")

