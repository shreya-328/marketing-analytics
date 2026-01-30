import pandas as pd

df = pd.read_csv("data/raw/raw_ads_performance_dirty.csv")

print("Shape: ",df.shape)
print("\nColumns : ",df.columns)
print("\nInfo: ",df.info())
print("Data Types: ",df.dtypes)

df=df[df["impressions"]!=0] #droppped invalid impression
print((df["impressions"]==0).sum())
print((df["conversions"].isna()).sum()) #identified missing conversion

df["conversion_missing_flag"]= df["conversions"].isna().astype(int)
print(df["conversion_missing_flag"].value_counts())

df["conversions"]=df["conversions"].fillna(0) #filled conversions safely

df["conversions"].isna().sum()
df["conversion_missing_flag"].sum()

# revenue NULL content
print("Revenue NULL count:",df["revenue"].isna().sum())
#revenue < 0 check
print("Revenue < 0 rows: ",(df["revenue"] < 0).sum())
# Cost = 0 but Revenue > 0 (logical error)
print(
    "Cost = 0 & Revenue > 0 rows:",
    ((df["cost"]==0) & (df["revenue"]>0)).sum()
)

# confirmation check
print("Impressions = 0 : ", (df["impressions"]==0).sum())
print("Conversions NULL : ",df["conversions"].isna().sum())
print("Conversion flag sum : ",df["conversion_missing_flag"].sum())

print(df["platform"].value_counts())

print(df["device"].value_counts())
print(df["campaign_type"].value_counts())
print(df["industry"].value_counts())
print(df["campaign_name"].nunique())
print(df["campaign_name"].head(10))


print(df["date"].head())
df["date"] = pd.to_datetime(df["date"])
print(df["date"].head())