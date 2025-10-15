import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Convert relevant columns to numerical values
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

#Plotting Grid
avg_msrp = df.groupby("Model Year")["Base MSRP"].mean()
plt.figure()
plt.plot(avg_msrp.index, avg_msrp.values, color="green", linewidth=2)
plt.title("Average Base MSRP per Model Year (Grid)")
plt.xlabel("Model Year")
plt.ylabel("Average Base MSRP ($)")
plt.grid(True)
plt.show()