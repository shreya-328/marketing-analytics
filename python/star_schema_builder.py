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
