import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#PART 3 for short or long range (nicholas) and long short and average range (chris)
i=input("Enter electric range")
if i==0:
        print("range has not been tested")
elif i>=100:
        print("long electric range")
else:
        print("short electric range")

# Ranges of electric vehicles
electric_ranges = [0, 0, 291, 84, 26, 293, 322, 6, 259, 53]
vehicle_names = ["Tesla Model S", "Kia EV6", "Tesla Model Y", "Fiat 500", "Kia Niro", 
                "Tesla Model X", "Tesla Model 3", "Toyota Prius", "Chevy Bolt", "Chevy Volt"]

print("Original vehicles:", vehicle_names)
print("Original ranges:", electric_ranges)
print()

# Filtering cars with 0 ranges
filtered_names = []
filtered_ranges = []

# Loop checking each automobile
for i in range(len(electric_ranges)):
    # Only keep vehicles that have been tested (range > 0)
    if electric_ranges[i] > 0:
        filtered_names.append(vehicle_names[i])
        filtered_ranges.append(electric_ranges[i])

print("After filtering out untested vehicles:")
print("Filtered vehicles:", filtered_names)
print("Filtered ranges:", filtered_ranges)
print()
print(f"We removed {len(vehicle_names) - len(filtered_names)} untested vehicles")

# Conditional for electric range
print("\n--- Range Classification ---")
n = int(input("Enter Electric Range: "))
if n == 0:
    print("Range has not been tested")
elif n <= 100:
    print("Short Range")
elif n > 100 and n <= 300:
    print("Average Range")
else:
    print("Long Range")

# Category each car falls into
print("\n--- Vehicle Categories ---")
for i in range(len(filtered_ranges)):
    if filtered_ranges[i] <= 100:
        category = "Short Range"
    elif filtered_ranges[i] <= 300:
        category = "Average Range"
    else:
        category = "Long Range"
    
    print(f"{filtered_names[i]}: {filtered_ranges[i]} miles → {category}")
    
#PART 4 Bar plot
# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Bar plot: Average Range by County (top 10)
# Purpose: compare how vehicle range differs by geographical region (county)
avg_by_county = df.groupby("County")["Electric Range"].mean().nlargest(10)
plt.figure(figsize=(8, 4))
plt.bar(avg_by_county.index, avg_by_county.values, color="teal")
plt.title("Average Electric Range by County")
plt.xlabel("County")
plt.ylabel("Average Range (miles)")
plt.xticks(rotation=45, ha="right")
plt.show()


#PART 4 Grid plot 
# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Grid plot: Average Base MSRP per Model Year
# Purpose: show MSRP trend over years with grid background for clarity
avg_msrp = df.groupby("Model Year")["Base MSRP"].mean()
plt.figure()
plt.plot(avg_msrp.index, avg_msrp.values, color="green", linewidth=2)
plt.title("Average Base MSRP per Model Year (Grid)")
plt.xlabel("Model Year")
plt.ylabel("Average Base MSRP ($)")
plt.grid(True)
plt.show()

#PART 4 pie charts
# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Pie chart: EV type distribution
# Purpose: see the market share (by count) of different electric vehicle types (BEV, PHEV, etc.)
type_counts = df["Electric Vehicle Type"].value_counts()
plt.figure()
plt.pie(type_counts.values, labels=type_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribution of Electric Vehicle Types")
plt.show()

