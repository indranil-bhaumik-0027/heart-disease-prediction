import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("heart.csv")

# Features and target
X = df[[
    'age',
    'sex',
    'cp',
    'trestbps',
    'chol',
    'fbs',
    'restecg',
    'thalach',
    'exang',
    'oldpeak',
    'slope',
    'ca',
    'thal'
]]

y = df['target']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("Model Accuracy:", round(acc * 100, 2), "%")

# Save model
with open("heart_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("heart_model.pkl created successfully")