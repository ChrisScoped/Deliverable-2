import pandas as pd
import matplotlib.pyplot as plt
# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Multi-line plot: Top 3 makes’ trends
# Purpose: compare how average range evolves over time for the three most common manufacturers
top_makes = df["Make"].value_counts().nlargest(3).index
plt.figure()
for make in top_makes:
    # For each make, compute year-wise average
    data = df[df["Make"] == make].groupby("Model Year")["Electric Range"].mean()
    plt.plot(data.index, data.values, label=make, linewidth=2)
plt.title("Average Electric Range by Model Year for Top 3 Makes")
plt.xlabel("Model Year")
plt.ylabel("Electric Range (miles)")
plt.legend()
plt.show()
