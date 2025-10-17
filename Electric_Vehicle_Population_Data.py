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
        
# I'm for now using only 25 samples to avoid messy plots
maker_col = df["Make"].head(25)

plt.hist(maker_col)

maker_without_tesla = []

# I'm removing tesla from my dataset
for make in maker_col:
    if make != "TESLA":
        maker_without_tesla.append(make)


print(df["Base MSRP"])
#plotting data points for x (make) and y (model year)
x_data=df["Make"].head(25)
y_data=df["Model Year"].head(25)
#printing and labeling scatter plot
plt.figure(figsize=(15,12))
plt.title("Scatter Plot Make v. Year")
plt.xlabel("Make")
plt.ylabel("Model Year")
plt.scatter(x_data, y_data)

df_filtered = df[df["Electric Range"] > 29]
print(df_filtered.head())
df_filtered.to_csv("filtered_output.csv", index=False)

#part 3 filtering the long

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

#PART 4 histogram 
# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

#Histrogram: Distribution of Electric Range
# Purpose: compare electric range to number of vehicles
ranges = df["Electric Range"].dropna()
plt.figure(figsize=(8, 5))
plt.hist(ranges, bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Count of Vehicles")
plt.grid(axis="y", alpha=0.75)
plt.show()

#PART 4 subplots 
# Convert relevant columns to numeric types (force invalid strings to NaN)
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
df["Base MSRP"] = pd.to_numeric(df["Base MSRP"], errors="coerce")

# Side-by-side subplots: histogram + bar
# Purpose: show a distribution and a categorical count next to each other for comparison
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(df["Electric Range"].dropna(), bins=20, color="skyblue")
# Left subplot: histogram of Electric Range distribution
axes[0].set_title("Distribution of Electric Range")
axes[0].set_xlabel("Electric Range (miles)")
axes[0].set_ylabel("Frequency")
# Right subplot: bar plot of counts of the top 5 makes
top_makes_count = df["Make"].value_counts().nlargest(5)
axes[1].bar(top_makes_count.index, top_makes_count.values, color="orange")
axes[1].set_title("Top 5 Vehicle Makes")
axes[1].set_xlabel("Make")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=45)
plt.suptitle("Subplots: Histogram & Bar")
plt.show()
