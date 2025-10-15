import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Convert relevant columns to numerical values
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

#Pie Chart
type_counts = df["Electric Vehicle Type"].value_counts()
plt.figure()
plt.pie(type_counts.values, labels=type_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribution of Electric Vehicle Types")
plt.show()