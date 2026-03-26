import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# 1️⃣ Load Data
# -----------------------------
X = pd.read_csv("X_processed.csv")
y = pd.read_csv("y.csv")

# -----------------------------
# 2️⃣ Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3️⃣ Train Best Model
# -----------------------------
model = RandomForestRegressor()
model.fit(X_train, y_train.values.ravel())

# -----------------------------
# 4️⃣ Save Model
# -----------------------------
joblib.dump(model, "model.pkl")

print("✅ Model saved as model.pkl")