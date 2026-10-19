import pandas as pd

calendar = pd.read_csv("data\\calendar.csv")
sales = pd.read_csv("data\\sales_train_validation.csv")
prices = pd.read_csv("data\\sell_prices.csv")


print("===== MISSING VALUE =====")

print("\nCalendar:")
print(calendar.isna().sum())

print("\nSales:")
print(sales.isna().sum())

print("\nPrices:")
print(prices.isna().sum())


print("\n===== DUPLICATE =====")

print("Calendar:", calendar.duplicated().sum())
print("Sales:", sales.duplicated().sum())
print("Prices:", prices.duplicated().sum())