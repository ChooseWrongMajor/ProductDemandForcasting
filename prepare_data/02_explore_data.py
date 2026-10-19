import pandas as pd

calendar = pd.read_csv("calendar.csv")

print("5 dòng đầu:")
print(calendar.head())

print("\n5 dòng cuối:")
print(calendar.tail())

print("\nKích thước:")
print(calendar.shape)

print("\nTên các cột:")
print(calendar.columns.tolist())

print("\nKiểu dữ liệu:")
print(calendar.dtypes)

print("\nThông tin:")
calendar.info()