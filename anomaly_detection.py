import joblib
import pandas as pd

model = joblib.load("anomaly_detector.pkl")

def detect_anomalies(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return "Anomaly" if prediction[0] == -1 else "Normal"