import pandas as pd


calendar = pd.read_csv("data\\calendar.csv")
sales = pd.read_csv("data\\sales_train_validation.csv")
prices = pd.read_csv("data\\sell_prices.csv")


# Chuyển date
calendar["date"] = pd.to_datetime(
    calendar["date"]
)


# ============================================================
# SALES
# ============================================================

sales_sample = sales.head(100).copy()


day_columns = [
    column
    for column in sales_sample.columns
    if column.startswith("d_")
][:30]


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


# ============================================================
# MELT
# ============================================================

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


# ============================================================
# MERGE CALENDAR
# ============================================================

result = pd.merge(
    sales_long,
    calendar,
    left_on="day",
    right_on="d",
    how="left"
)

print("Sau merge với calendar:")
print(result.head())


# ============================================================
# MERGE PRICES
# ============================================================

result = pd.merge(
    result,
    prices,
    on=[
        "store_id",
        "item_id",
        "wm_yr_wk"
    ],
    how="left"
)


print("\nSau merge với prices:")
print(result.head())


print("\nShape:")
print(result.shape)