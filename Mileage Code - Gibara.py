import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# I'm for now using only 20 samples to avoid messy plots
maker_col = df["Make"].head(20)

plt.hist(maker_col)

maker_without_tesla = []

# I'm removing tesla from my dataset
for make in maker_col:
    if make != "TESLA":
        maker_without_tesla.append(make)


print(df["Base MSRP"])

plt.figure(figsize=(18,6))
sns.relplot(data=df, x=maker_col, y=df["Model Year"].head(20), hue="Electric Vehicle Type")







#n=int(input("Enter Electric Range:"))
#if n == 0:
#  print("Range has not been tested")
#elif n<= 100:
#        print("Short Range")
#elif n > 100 and n <= 300 :
#        print("Average Range")
#else:
#        print("Long Range")        
    