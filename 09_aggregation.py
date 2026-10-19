import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


# Tìm tất cả cột ngày
day_columns = [
    column
    for column in sales.columns
    if column.startswith("d_")
]

print("Số ngày:", len(day_columns))


# Tổng sales của từng sản phẩm
sales["total_sales"] = sales[
    day_columns
].sum(axis=1)


print("\nTổng sales của 10 sản phẩm đầu:")
print(
    sales[
        ["item_id", "store_id", "total_sales"]
    ].head(10)
)


# Tổng sales theo store
result = sales.groupby(
    "store_id"
)["total_sales"].sum()

print("\nTổng sales theo store:")
print(result)


# Tổng sales theo category
result = sales.groupby(
    "cat_id"
)["total_sales"].sum()

print("\nTổng sales theo category:")
print(result)