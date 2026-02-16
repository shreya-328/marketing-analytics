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