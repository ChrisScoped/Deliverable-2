import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Convert relevant columns to numerical values
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

#Histrogram
ranges = df["Electric Range"].dropna()
plt.figure(figsize=(8, 5))
plt.hist(ranges, bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Count of Vehicles")
plt.grid(axis="y", alpha=0.75)
plt.show()