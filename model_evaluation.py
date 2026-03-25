import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# 1️⃣ Load Processed Data
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
# 3️⃣ Define Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

results = {}

# -----------------------------
# 4️⃣ Train + Evaluate
# -----------------------------
for name, model in models.items():
    model.fit(X_train, y_train.values.ravel())
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions, squared=False)

    results[name] = {"R2 Score": r2, "RMSE": rmse}

    print(f"{name} → R2: {r2:.3f}, RMSE: {rmse:.3f}")

# -----------------------------
# 5️⃣ Find Best Model
# -----------------------------
best_model = max(results, key=lambda x: results[x]["R2 Score"])

print("\n🏆 Best Model:", best_model)