import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

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

