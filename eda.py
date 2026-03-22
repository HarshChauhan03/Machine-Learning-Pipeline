# Day 3 - Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Load Clean Dataset
# -----------------------------
df = pd.read_csv("clean_data.csv")

print("Dataset Loaded for EDA\n")

# -----------------------------
# 2️⃣ Basic Statistics
# -----------------------------
print("🔹 Statistical Summary:")
print(df.describe())

# -----------------------------
# 3️⃣ Correlation Matrix
# -----------------------------
print("\n🔹 Correlation Matrix:")
print(df.corr(numeric_only=True))

# -----------------------------
# 4️⃣ Plot Distribution (Histogram)
# -----------------------------
df.hist(figsize=(10, 8))
plt.suptitle("Feature Distributions")
plt.show()

# -----------------------------
# 5️⃣ Scatter Plot (Example)
# -----------------------------
if "area" in df.columns and "price" in df.columns:
    plt.scatter(df["area"], df["price"])
    plt.xlabel("Area")
    plt.ylabel("Price")
    plt.title("Area vs Price")
    plt.show()

# -----------------------------
# 6️⃣ Correlation Heatmap (Manual)
# -----------------------------
import numpy as np

corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
plt.imshow(corr, interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()