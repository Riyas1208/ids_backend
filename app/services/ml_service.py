import os, joblib, numpy as np
MODEL_PATH = os.getenv('MODEL_PATH','app/ml/rf_model.joblib')
_art = None

def load_model():
    global _art
    if _art is None and os.path.exists(MODEL_PATH):
        _art = joblib.load(MODEL_PATH)
    return _art

def predict_df(df):
    art = load_model()
    if art is None:
        preds = np.random.choice([0,1], size=len(df), p=[0.88,0.12])
        probs = np.random.random(len(df))
        return preds, probs
    model = art.get('model')
    cols = art.get('feature_cols', df.columns.tolist())
    X = df[cols].astype(float).values
    scaler = art.get('scaler')
    if scaler is not None:
        X = scaler.transform(X)
    preds = model.predict(X).astype(int)
    probs = model.predict_proba(X)[:,1] if hasattr(model, 'predict_proba') else np.zeros(len(preds))
    return preds, probs
