import pandas as pd
import io

def parse_csv_bytes(content: bytes, max_rows: int | None = None):
    try:
        df = pd.read_csv(io.BytesIO(content))
    except Exception:
        s = content.decode('utf-8', errors='ignore')
        df = pd.read_csv(io.StringIO(s))
    if max_rows and len(df) > max_rows:
        return df.head(max_rows)
    return df
