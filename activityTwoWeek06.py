import pandas as pd
import matplotlib.pyplot as plt

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

# 5. Plot grouped bar chart
plt.figure(figsize=(6, 4))
plt.bar(["Route 1", "Route 2"], [route1_total, route2_total], color=["steelblue", "orange"])
plt.ylabel("Total Estimated Vehicle Density (Rho)")
plt.title("Route 1 vs Route 2 Estimated Density")
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()