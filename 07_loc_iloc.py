import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


print("===== LOC =====")

result = sales.loc[
    sales["store_id"] == "CA_1",
    ["item_id", "cat_id", "store_id"]
]

print(result.head())


print("\n===== ILOC =====")

result = sales.iloc[0:5, 0:5]

print(result)