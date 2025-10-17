import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#part 3 for short or long range
i=input("Enter electric range")
if i==0:
        print("range has not been tested")
elif i>=100:
        print("long electric range")
else:
        print("short electric range")

