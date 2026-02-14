import pandas as pd
import numpy as np
from scipy import stats
from math import erf, sqrt

# 1. Load data
file_path = file_path = r"F:\Master of Software Engineering (Level 9)\Trimester 02\MSE803 Data Analytics\Week_08_08022026\Retail_Dataset_Week5_7_Mukesh.xlsx"
df = pd.read_excel(file_path)

# 2. Split Sales Amount by segment
consumer = df[df["Customer Segment"] == "Consumer"]["Sales Amount"]
corporate = df[df["Customer Segment"] == "Corporate"]["Sales Amount"]

alpha = 0.05
# (1) Independent T-Test
t_stat, t_p = stats.ttest_ind(consumer, corporate, equal_var=True)

print("T-TEST RESULTS")
print("t statistic:", t_stat)
print("p value   :", t_p)

if t_p < alpha:
    print("Significant Difference")
else:
    print("No Significant Difference")
print()

# (2) Approximate Z-Test

n1, n2 = len(consumer), len(corporate)
mean1, mean2 = consumer.mean(), corporate.mean()
var1, var2 = consumer.var(ddof=1), corporate.var(ddof=1)

se = np.sqrt(var1/n1 + var2/n2)
z_stat = (mean1 - mean2) / se

# two-sided p-value from standard normal
p_z = 2 * (1 - 0.5 * (1 + erf(abs(z_stat) / sqrt(2))))

print("Z-TEST RESULTS")
print("z statistic:", z_stat)
print("p value   :", p_z)
if p_z < alpha:
    print("Significant Difference")
else:
    print("No Significant Difference")
print()

# (3) One-Way ANOVA

f_stat, f_p = stats.f_oneway(consumer, corporate)

print("ANOVA RESULTS")
print("F statistic:", f_stat)
print("p value   :", f_p)
if f_p < alpha:
    print("Significant Difference")
else:
    print("No Significant Difference")
