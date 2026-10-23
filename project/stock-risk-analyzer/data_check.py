from src.load_data import load_prices

df = load_prices("data/prices.csv")

print(df.head())
print(df.info())
print(df.groupby("asset").size())

