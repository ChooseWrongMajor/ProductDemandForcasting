import pandas as pd

sales = pd.read_csv("data\\sales_train_validation.csv")


print("===== THEO STORE =====")

result = sales.groupby(
    "store_id"
)["item_id"].count()

print(result)


print("\n===== THEO CATEGORY =====")

result = sales.groupby(
    "cat_id"
)["item_id"].count()

print(result)


print("\n===== THEO STATE =====")

result = sales.groupby(
    "state_id"
)["item_id"].count()

print(result)