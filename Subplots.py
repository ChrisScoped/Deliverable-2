import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Convert relevant columns to numerical values
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

#Subplots for dataset
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(df["Electric Range"].dropna(), bins=20, color="skyblue")
axes[0].set_title("Distribution of Electric Range")
axes[0].set_xlabel("Electric Range (miles)")
axes[0].set_ylabel("Frequency")
top_makes_count = df["Make"].value_counts().nlargest(5)
axes[1].bar(top_makes_count.index, top_makes_count.values, color="orange")
axes[1].set_title("Top 5 Vehicle Makes")
axes[1].set_xlabel("Make")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=45)
plt.suptitle("Subplots: Histogram & Bar")
plt.show()