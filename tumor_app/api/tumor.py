from tumor_app.db.schema import TumorPredict
from fastapi import APIRouter
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


tumor_router = APIRouter(prefix='/tumor', tags=['Tumor'])

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_svm_path = BASE_DIR / 'model_svm.pkl'
scaler_path = BASE_DIR / 'scaler.pkl'

model_svm = joblib.load(model_svm_path)
scaler = joblib.load(scaler_path)

@tumor_router.post('/predict/')
async def predict(tumor_data: TumorPredict):
    tumor_data_dict = tumor_data.dict()

    features = list(tumor_data_dict.values())
    scaled = scaler.transform([features])
    prediction = model_svm.predict(scaled)[0]
    # probability = model_svm.predict_proba(scaled)[0][1]
    return {'prediction': prediction}
