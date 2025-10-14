import pandas as pd
df = pd.read_csv(r"C:\Users\Chris\Documents\GitHub\Deliverable-2\Electric_Vehicle_Population_Data.csv")
df_filtered = df[df["Electric Range"] > 29]
print(df_filtered.head())
df_filtered.to_csv("filtered_output.csv", index=False)