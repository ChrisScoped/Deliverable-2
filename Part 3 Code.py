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