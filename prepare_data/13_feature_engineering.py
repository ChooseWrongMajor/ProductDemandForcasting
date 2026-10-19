import pandas as pd

calendar = pd.read_csv("data\\calendar.csv")


calendar["date"] = pd.to_datetime(
    calendar["date"]
)


# Tạo năm
calendar["year"] = calendar[
    "date"
].dt.year


# Tạo tháng
calendar["month"] = calendar[
    "date"
].dt.month


# Tạo ngày
calendar["day"] = calendar[
    "date"
].dt.day


# Tạo thứ trong tuần
calendar["day_of_week"] = calendar[
    "date"
].dt.dayofweek


print(
    calendar[
        [
            "date",
            "year",
            "month",
            "day",
            "day_of_week"
        ]
    ].head(10)
)