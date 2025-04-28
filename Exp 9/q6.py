import pandas as pd
data = {"Rohan": 176, "John": 175, "Harvinder": 180, "Hasan": 174}
X = pd.Series(data, index=["Tinku", "John", "Ramesh", "Hasan"])
print("Series X:\n", X)
print("NaN indices:", X[X.isna()].index.tolist())