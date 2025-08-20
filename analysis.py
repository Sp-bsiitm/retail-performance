import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Compute average
average = df["Turnover"].mean()
print("Average Inventory Turnover:", round(average, 2))  # 7.39

# Plot
plt.plot(df["Quarter"], df["Turnover"], marker="o", label="Company Turnover")
plt.axhline(y=8, color="r", linestyle="--", label="Industry Target (8)")
plt.title("Quarterly Inventory Turnover Ratio (2024)")
plt.xlabel("Quarter")
plt.ylabel("Turnover Ratio")
plt.legend()
plt.savefig("charts/turnover_trend.png", dpi=300)
plt.close()
