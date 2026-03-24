# Day 5 - Model Training

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# 1️⃣ Load Processed Data
# -----------------------------
X = pd.read_csv("X_processed.csv")
y = pd.read_csv("y.csv")

print("Data Loaded for Model Training\n")

# -----------------------------
# 2️⃣ Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train-Test Split Done\n")

# -----------------------------
# 3️⃣ Define Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

# -----------------------------
# 4️⃣ Train Models
# -----------------------------
trained_models = {}

for name, model in models.items():
    model.fit(X_train, y_train.values.ravel())
    trained_models[name] = model
    print(f"{name} trained successfully")

print("\nAll models trained")