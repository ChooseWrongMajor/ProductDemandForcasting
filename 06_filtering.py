import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


# Lọc store CA_1
ca1 = sales[
    sales["store_id"] == "CA_1"
]

print("Sản phẩm của CA_1:")
print(ca1.head())


# Lọc category FOODS
foods = sales[
    sales["cat_id"] == "FOODS"
]

print("\nSản phẩm thuộc FOODS:")
print(foods.head())


# Lọc CA_1 + FOODS
result = sales[
    (sales["store_id"] == "CA_1") &
    (sales["cat_id"] == "FOODS")
]

print("\nCA_1 + FOODS:")
print(result.head())


# Lọc nhiều store
result = sales[
    sales["store_id"].isin(["CA_1", "CA_2"])
]

print("\nCA_1 hoặc CA_2:")
print(result.head())