import pandas as pd

PRICE = 3.49  # price per bar in USD

df = pd.read_csv("data/q3_2026_sales.csv")
df["units_sold"] = df["units_sold"].fillna(0)
df["revenue"] = df["units_sold"] * PRICE

by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print(by_product)
print("Total Q3 revenue:", round(df["revenue"].sum(), 2))
print("Average monthly revenue:", round(df.groupby("month")["revenue"].sum().mean(), 2))
