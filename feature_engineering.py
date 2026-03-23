# Day 4 - Feature Engineering

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# -----------------------------
# 1️⃣ Load Clean Dataset
# -----------------------------
df = pd.read_csv("clean_data.csv")

print("Dataset Loaded for Feature Engineering\n")

# -----------------------------
# 2️⃣ Separate Features & Target
# -----------------------------
X = df.drop("price", axis=1)
y = df["price"]

# -----------------------------
# 3️⃣ Handle Categorical Data
# -----------------------------
label_encoders = {}

for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

print("Categorical Encoding Done")

# -----------------------------
# 4️⃣ Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print("Feature Scaling Done")

# -----------------------------
# 5️⃣ Save Processed Data
# -----------------------------
X_scaled.to_csv("X_processed.csv", index=False)
y.to_csv("y.csv", index=False)

print("Processed data saved (X_processed.csv, y.csv)")