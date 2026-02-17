import pandas as pd

df= pd.read_csv("data/raw/raw_ads_performance_dirty.csv")

#cleaning platform column
df["platform"] = df["platform"].str.strip().str.title()

print(df["platform"].head())

# extracting unique platforms
platforms = df["platform"].drop_duplicates()

# sorting alphabetically
platforms = platforms.sort_values().reset_index(drop=True)

#converting to dataframe
dim_platform = platforms.to_frame()

#assigning stable sequential IDs
dim_platform["platform_id"] = dim_platform.index +1 

#reordering columns
dim_platforms = dim_platform[["platform_id","platform"]]
print(platforms)


# FOR device
df["device"] = df["device"].str.strip().str.title()

# extraction
devices = df["device"].drop_duplicates()

#sorting
devices = devices.sort_values().reset_index(drop=True)

#convert to dataframe
dim_device = devices.to_frame()

#assing surrogate ids
dim_device["device_id"]=dim_device.index + 1

#reordering columns 
dim_device = dim_device[["device_id","device"]]
print(dim_device)

# dim_campaign
df["campaign_name"] = df["campaign_name"].str.strip().str.title()
df["campaign_type"] = df["campaign_type"].str.strip().str.title()
df["industry"] = df["industry"].str.strip().str.title()

# removing duplicates
campaigns = df[["campaign_name", "campaign_type", "industry"]].drop_duplicates()

print(campaigns.head())
print("Total unique campaigns:", len(campaigns))

campaigns = campaigns.sort_values(
    by=["campaign_name", "campaign_type", "industry"]
).reset_index(drop=True)

print(campaigns.head())

#sorting

campaigns = campaigns.sort_values(
    by=["campaign_name", "campaign_type", "industry"]
).reset_index(drop=True)

print(campaigns.head())

#assigning campaign id
dim_campaign = campaigns.copy()

dim_campaign["campaign_id"] = dim_campaign.index + 1

# Reorder columns (ID first)
dim_campaign = dim_campaign[
    ["campaign_id", "campaign_name", "campaign_type", "industry"]
]

print(dim_campaign.head())
print("Total campaigns in dimension:", len(dim_campaign))

# creating dim_date 

# identifying the min and max date
print("Min date: ",df["date"].min())
print("Max date: ",df["date"].max())

# creting a full date range

# Ensure date column is datetime (safety)
df["date"] = pd.to_datetime(df["date"])

# Create full date range
date_range = pd.date_range(
    start=df["date"].min(),
    end=df["date"].max(),
    freq="D"
)

print("Total days in calendar:", len(date_range))
print(date_range[:5])

#converting date_range into a dataframe and generating attrbutes

# Convert to dataframe
dim_date = pd.DataFrame({"full_date": date_range})

# Generate attributes
dim_date["year"] = dim_date["full_date"].dt.year
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["month_name"] = dim_date["full_date"].dt.month_name()
dim_date["quarter"] = dim_date["full_date"].dt.quarter
dim_date["day"] = dim_date["full_date"].dt.day
dim_date["day_name"] = dim_date["full_date"].dt.day_name()
dim_date["week"] = dim_date["full_date"].dt.isocalendar().week

# Assign stable date_id
dim_date["date_id"] = dim_date.index + 1

# Reorder columns
dim_date = dim_date[
    [
        "date_id",
        "full_date",
        "year",
        "month",
        "month_name",
        "quarter",
        "day",
        "day_name",
        "week"
    ]
]

print(dim_date.head())
print("Total dates in dimension:", len(dim_date))

# mergin platform for fact table

fact_df = df.merge(
    dim_platform,
    on="platform",
    how="left"
)

print(fact_df.head())
print("Null platform_id:", fact_df["platform_id"].isna().sum())

#merging dim_device
fact_df = fact_df.merge(
    dim_device,
    on="device",
    how="left"
)

print(fact_df.head())
print("Null device_id:", fact_df["device_id"].isna().sum())

#merging dim_campaign
fact_df = fact_df.merge(
    dim_campaign,
    on=["campaign_name", "campaign_type", "industry"],
    how="left"
)

print(fact_df.head())
print("Null campaign_id:", fact_df["campaign_id"].isna().sum())

#merging dim_date
fact_df = fact_df.merge(
    dim_date,
    left_on="date",
    right_on="full_date",
    how="left"
)

print("Null date_id:", fact_df["date_id"].isna().sum())
print(fact_df.head())

#building fact_ads_performance
fact_ads_performance = fact_df[
    [
        "date_id",
        "platform_id",
        "device_id",
        "campaign_id",
        "impressions",
        "clicks",
        "cost",
        "conversions",
        "revenue"
    ]
]

print(fact_ads_performance.head())
print("Fact table rows:", len(fact_ads_performance))

print(fact_ads_performance.isnull().sum())

fact_ads_performance["conversions"] = fact_ads_performance["conversions"].fillna(0)
fact_ads_performance["revenue"] = fact_ads_performance["revenue"].fillna(0)

# Create output folder if not exists
import os
os.makedirs("output", exist_ok=True)

# Export dimensions
dim_platform.to_csv("output/dim_platform.csv", index=False)
dim_device.to_csv("output/dim_device.csv", index=False)
dim_campaign.to_csv("output/dim_campaign.csv", index=False)
dim_date.to_csv("output/dim_date.csv", index=False)

# Export fact table
fact_ads_performance.to_csv("output/fact_ads_performance.csv", index=False)

print("✅ All tables exported successfully.")
