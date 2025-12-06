import pandas as pd

# Load the Excel file
file_path = r"F:\Master of Software Engineering (Level 9)\Trimester 02\MSE803 Data Analytics\Week_02_30112025\Week2_Mukesh.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Compute average passengers per route
avg_passengers = (df.groupby("Route_ID")["Passenger_Count"]
                    .mean()
                    .reset_index()
                    .rename(columns={"Passenger_Count": "Avg_Passenger_Count"})
                 )

print(f"Average passengers per route:\n {avg_passengers}")
max_row = avg_passengers.loc[avg_passengers["Avg_Passenger_Count"].idxmax()]
print(f"Route {int(max_row['Route_ID'])} with {max_row['Avg_Passenger_Count']:.2f} highest average passengers")
