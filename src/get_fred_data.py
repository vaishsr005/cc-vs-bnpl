# Download credit card and macro data from FRED and save it as raw files.

import os
from dotenv import load_dotenv
from fredapi import Fred

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("FRED_API_KEY")
if not api_key:
    raise SystemExit("No FRED_API_KEY found. Check your .env file.")

fred = Fred(api_key=api_key)

SERIES = {
    "DRCCLACBS": "cc_delinquency_rate",
    "CORCCACBS": "cc_chargeoff_rate",
    "UNRATE": "unemployment_rate",
}

# 4. Download each series and save it untouched in data/raw
for series_id, column_name in SERIES.items():
    data = fred.get_series(series_id)
    df = data.rename(column_name).to_frame()
    df.index.name = "date"
    df.to_csv(f"data/raw/{series_id}.csv")
    print(f"{series_id}: {len(df)} rows, "
          f"{df.index.min().date()} to {df.index.max().date()}")