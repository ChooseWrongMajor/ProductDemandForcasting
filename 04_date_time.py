import pandas as pd

calendar = pd.read_csv("data\\calendar.csv")

print("Kiểu dữ liệu ban đầu:")
print(calendar["date"].dtype)


calendar["date"] = pd.to_datetime(calendar["date"])


print("\nKiểu dữ liệu sau khi chuyển:")
print(calendar["date"].dtype)


print("\nNăm:")
print(calendar["date"].dt.year.head())

print("\nTháng:")
print(calendar["date"].dt.month.head())

print("\nNgày:")
print(calendar["date"].dt.day.head())

print("\nThứ trong tuần:")
print(calendar["date"].dt.dayofweek.head())