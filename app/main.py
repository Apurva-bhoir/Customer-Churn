import pandas as pd
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Example raw input
raw_data = {
    "gender": ["Female"],
    "SeniorCitizen": [0],
    "Partner": ["Yes"],
    "Dependents": ["No"],
    "tenure": [1],
    "PhoneService": ["No"],
    "MultipleLines": ["No phone service"],
    "InternetService": ["DSL"],
    "OnlineSecurity": ["No"],
    "OnlineBackup": ["Yes"],
    "DeviceProtection": ["No"],
    "TechSupport": ["No"],
    "StreamingTV": ["No"],
    "StreamingMovies": ["No"],
    "Contract": ["Month-to-month"],
    "PaperlessBilling": ["Yes"],
    "PaymentMethod": ["Electronic check"],
    "MonthlyCharges": [29.85],
    "TotalCharges": [29.85]
}
df = pd.DataFrame(raw_data)

# Re-apply training preprocessing (must match your training script!)
df_encoded = pd.get_dummies(df)

# Align with training columns
train_columns = model.feature_names_in_
df_encoded = df_encoded.reindex(columns=train_columns, fill_value=0)

# Predict
prediction = model.predict(df_encoded)
print("Prediction:", prediction)
print("Customer is likely to churn" if prediction[0] == 1 else "Customer will stay")
