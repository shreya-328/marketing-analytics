import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/raw_ads_performance_dirty.csv")

# Cleaning
df = df[df["impressions"] != 0]
df["conversions"] = df["conversions"].fillna(0)
df["revenue"] = df["revenue"].fillna(0)

# ROAS
df = df[df["cost"] > 0]
df["ROAS"] = df["revenue"] / df["cost"]

# -----------------------------
# Plot 1: ROAS by Campaign Type
# -----------------------------
plt.figure(figsize=(8,5))
df.boxplot(column="ROAS", by="campaign_type")
plt.title("ROAS by Campaign Type")
plt.suptitle("")
plt.xlabel("Campaign Type")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig("outputs/roas_by_campaign_type.png")
plt.close()

# -----------------------------
# Plot 2: ROAS by Device
# -----------------------------
plt.figure(figsize=(8,5))
df.boxplot(column="ROAS", by="device")
plt.title("ROAS by Device")
plt.suptitle("")
plt.xlabel("Device")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig("outputs/roas_by_device.png")
plt.close()

# -----------------------------
# Plot 3: Conversion Rate by Device
# -----------------------------
device_conv = df.groupby("device")[["clicks", "conversions"]].sum()
device_conv["conversion_rate"] = device_conv["conversions"] / device_conv["clicks"]

plt.figure(figsize=(6,4))
device_conv["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Device")
plt.xlabel("Device")
plt.ylabel("Conversion Rate")
plt.tight_layout()
plt.savefig("outputs/conversion_rate_by_device.png")
plt.close()

df["CPA"] = np.where(
    df["conversions"] > 0,
    df["cost"] / df["conversions"],
    np.nan
)

plt.figure(figsize=(7,5))
plt.scatter(df["conversions"], df["CPA"], alpha=0.5)
plt.xlabel("Conversions")
plt.ylabel("CPA")
plt.title("CPA vs Conversions")
plt.tight_layout()
plt.savefig("outputs/cpa_vs_conversions.png")
plt.close()

plt.figure(figsize=(7,5))
plt.scatter(df["clicks"], df["cost"], alpha=0.5)
plt.xlabel("Clicks")
plt.ylabel("Cost")
plt.title("Clicks vs Cost")
plt.tight_layout()
plt.savefig("outputs/clicks_vs_cost.png")
plt.close()

# Ensure date is datetime
df["date"] = pd.to_datetime(df["date"])

# Create month column
df["month"] = df["date"].dt.to_period("M")

# Monthly aggregation
monthly = df.groupby("month")[["revenue", "cost"]].sum()

# ROAS calculation
monthly["ROAS"] = monthly["revenue"] / monthly["cost"]

# Convert period to timestamp for plotting
monthly.index = monthly.index.to_timestamp()

# Plot
plt.figure(figsize=(8,4))
plt.plot(monthly.index, monthly["ROAS"], marker="o")
plt.title("Monthly ROAS Trend")
plt.xlabel("Month")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig("outputs/monthly_roas_trend.png")