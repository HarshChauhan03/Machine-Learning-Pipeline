# Day 2 - Data Preprocessing

import pandas as pd

# -----------------------------
# 1️⃣ Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

print("Dataset Loaded\n")

# -----------------------------
# 2️⃣ Check Missing Values
# -----------------------------
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# -----------------------------
# 3️⃣ Handle Missing Values
# -----------------------------

# Fill numerical columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical columns with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -----------------------------
# 4️⃣ Remove Duplicates
# -----------------------------
df.drop_duplicates(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates Removed")

# -----------------------------
# 5️⃣ Fix Data Types
# -----------------------------
# Example: convert date column (if exists)

if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# 6️⃣ Save Clean Data
# -----------------------------
df.to_csv("clean_data.csv", index=False)

print("\nClean dataset saved as clean_data.csv")