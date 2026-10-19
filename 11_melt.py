import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


# Chỉ lấy 100 sản phẩm
sales_sample = sales.head(100).copy()


# Tìm các cột ngày
day_columns = [
    column
    for column in sales_sample.columns
    if column.startswith("d_")
]


# Chỉ lấy 30 ngày đầu
day_columns = day_columns[:30]


# Chọn các cột cần thiết
sales_sample = sales_sample[
    [
        "id",
        "item_id",
        "dept_id",
        "cat_id",
        "store_id",
        "state_id"
    ] + day_columns
]


print("===== TRƯỚC MELT =====")

print(sales_sample.head())


# MELT
sales_long = sales_sample.melt(
    id_vars=[
        "id",
        "item_id",
        "dept_id",
        "cat_id",
        "store_id",
        "state_id"
    ],
    var_name="day",
    value_name="sales"
)


print("\n===== SAU MELT =====")

print(sales_long.head(20))

print("\nShape:")
print(sales_long.shape)