import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


day_columns = [
    column
    for column in sales.columns
    if column.startswith("d_")
]


sales["total_sales"] = sales[
    day_columns
].sum(axis=1)


result = sales.sort_values(
    "total_sales",
    ascending=False
)


print("10 sản phẩm bán nhiều nhất:")

print(
    result[
        [
            "item_id",
            "store_id",
            "total_sales"
        ]
    ].head(10)
)