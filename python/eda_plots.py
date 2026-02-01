import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/raw_ads_performance_dirty.csv")

df = df[df["impressions"] != 0]
df["conversions"] = df["conversions"].fillna(0)

plt.hist(df["impressions"], bins=30)
plt.title("Distribution of Impressions")
plt.xlabel("Impressions")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["impressions"], df["clicks"], alpha=0.5)
plt.title("Impressions vs Clicks")
plt.xlabel("Impressions")
plt.ylabel("Clicks")
plt.show()

plt.figure()
plt.scatter(df["clicks"], df["conversions"])
plt.xlabel("Clicks")
plt.ylabel("Conversions")
plt.title("Clicks vs Conversions")
plt.show()

# Cost vs Revenue scatter plot
plt.scatter(df["cost"], df["revenue"], alpha=0.5)
plt.title("Cost vs Revenue")
plt.xlabel("Cost")
plt.ylabel("Revenue")
plt.show()
