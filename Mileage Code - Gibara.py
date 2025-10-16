import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered CSV dataset
df = pd.read_csv("filtered_output.csv")

# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")
# Scatter plot: Electric Range vs Model Year
# Purpose: examine correlation / spread: do newer years have higher range?
plt.figure()
plt.scatter(df["Model Year"], df["Electric Range"], alpha=0.6)
plt.title("Electric Range vs Model Year")
plt.xlabel("Model Year")
plt.ylabel("Electric Range (miles)")
plt.show()