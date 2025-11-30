from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.schemas import AnalyzeSummary
from app.utils.csv_utils import parse_csv_bytes
from app.services.ml_service import predict_df
from datetime import datetime
router = APIRouter()

@router.post('/', response_model=AnalyzeSummary)
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    try:
        df = parse_csv_bytes(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Cannot parse CSV: {e}')
    preds, probs = predict_df(df)
    total = len(df)
    attack_count = int((preds == 1).sum())
    normal_count = total - attack_count
    return AnalyzeSummary(file=file.filename, total_rows=total, attack_count=attack_count, normal_count=normal_count, timestamp=datetime.utcnow())
