import pandas as pd

# -----------------------------
# 1️⃣ Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

print("✅ Dataset Loaded Successfully\n")

# -----------------------------
# 2️⃣ Show First Rows
# -----------------------------
print("🔹 First 5 Rows:")
print(df.head())

# -----------------------------
# 3️⃣ Dataset Shape
# -----------------------------
print("\n🔹 Shape (Rows, Columns):")
print(df.shape)

# -----------------------------
# 4️⃣ Column Names
# -----------------------------
print("\n🔹 Columns:")
print(df.columns)

# -----------------------------
# 5️⃣ Dataset Info
# -----------------------------
print("\n🔹 Dataset Info:")
df.info()

# -----------------------------
# 6️⃣ Missing Values
# -----------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# -----------------------------
# 7️⃣ Basic Statistics
# -----------------------------
print("\n🔹 Statistical Summary:")
print(df.describe())