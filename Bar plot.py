import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Convert relevant columns to numerical values
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Bar Plot
avg_by_county = df.groupby("County")["Electric Range"].mean().nlargest(10)
plt.figure(figsize=(8, 4))
plt.bar(avg_by_county.index, avg_by_county.values, color="teal")
plt.title("Average Electric Range by County")
plt.xlabel("County")
plt.ylabel("Average Range (miles)")
plt.xticks(rotation=45, ha="right")
plt.show()
