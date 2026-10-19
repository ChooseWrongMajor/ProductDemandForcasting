import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


print("===== UNIQUE =====")

print("\nCác state:")
print(sales["state_id"].unique())

print("\nCác store:")
print(sales["store_id"].unique())

print("\nCác category:")
print(sales["cat_id"].unique())


print("\n===== VALUE COUNTS =====")

print("\nSố sản phẩm theo category:")
print(sales["cat_id"].value_counts())

print("\nSố sản phẩm theo store:")
print(sales["store_id"].value_counts())

print("\nSố sản phẩm theo state:")
print(sales["state_id"].value_counts())