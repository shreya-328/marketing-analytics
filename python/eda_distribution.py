import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("data/raw/raw_ads_performance_dirty.csv")

# Basic cleaning (same jo tum already kar chuki ho)
df = df[df["impressions"] != 0]
df["conversions"] = df["conversions"].fillna(0)
df["revenue"] = df["revenue"].fillna(0)

# ROAS calculation
df["ROAS"] = df["revenue"] / df["cost"]
df = df[df["cost"] > 0]   # safety check

# Boxplot: Campaign Type vs ROAS
plt.figure()
df.boxplot(column="ROAS", by="campaign_type")
plt.title("ROAS by Campaign Type")
plt.suptitle("")  # default title remove
plt.xlabel("Campaign Type")
plt.ylabel("ROAS")
plt.show()