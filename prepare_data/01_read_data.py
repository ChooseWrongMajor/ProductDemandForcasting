import pandas as pd

calendar = pd.read_csv("data\\calendar.csv")
sales = pd.read_csv("data\\sales_train_validation.csv")
prices = pd.read_csv("data\\sell_prices.csv")


print("\nCalendar:")
print(calendar.head())

print("\nSales:")
print(sales.head())

print("\nPrices:")
print(prices.head())