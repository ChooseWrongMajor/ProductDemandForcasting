import pandas as pd


calendar = pd.read_csv("data\\calendar.csv")
sales = pd.read_csv("data\\sales_train_validation.csv")


calendar["date"] = pd.to_datetime(
    calendar["date"]
)


# Lấy 100 sản phẩm
sales_sample = sales.head(100).copy()


# Lấy 30 ngày
day_columns = [
    column
    for column in sales_sample.columns
    if column.startswith("d_")
][:30]


sales_sample = sales_sample[
    [
        "id",
        "item_id",
        "store_id"
    ] + day_columns
]


# Chuyển wide → long
sales_long = sales_sample.melt(
    id_vars=[
        "id",
        "item_id",
        "store_id"
    ],
    var_name="day",
    value_name="sales"
)


# Ghép calendar
sales_long = pd.merge(
    sales_long,
    calendar,
    left_on="day",
    right_on="d",
    how="left"
)


# Pivot
pivot = pd.pivot_table(
    sales_long,
    values="sales",
    index="date",
    columns="store_id",
    aggfunc="sum"
)


print(pivot.head(20))