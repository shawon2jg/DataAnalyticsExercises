import pandas as pd

# 1. Load the Excel sheet
file_path = r"F:\Master of Software Engineering (Level 9)\Trimester 02\MSE806 Intelligent Transportation Systems\Week_04_13122025\Case_Study_Table.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 2. Compute Estimated Rho for each road segment
df["Estimated Rho"] = (
    df["Alpha"] * df["Current Rho"] +
    (1 - df["Alpha"]) * df["Past Rho"]
)

# 3. Define the two routes
route1_ids = ["FG", "GB", "BD(School)", "DP"]      # F-G-B-D-P
route2_ids = ["FH", "HM", "MN", "NP"]              # F-H-M-N-P

# 4. Sum estimated densities along each route
route1_total = df[df["Road ID"].isin(route1_ids)]["Estimated Rho"].sum()
route2_total = df[df["Road ID"].isin(route2_ids)]["Estimated Rho"].sum()

# 5. Decide which route is better (lower total density)
better_route = "Route 1 (F-G-B-D-P)" if route1_total < route2_total else "Route 2 (F-H-M-N-P)"

print("Route 1 total estimated rho:", route1_total)
print("Route 2 total estimated rho:", route2_total)
print("Better Route:", better_route)
