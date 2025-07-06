from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()

@router.get("/transactions")
def get_aggregated_transactions(year: int = None, quarter: int = None):
    df = pd.read_csv("exports/transformed/aggregated_transaction.csv")

    if year is not None:
        df = df[df['year'] == year]
    if quarter is not None:
        df = df[df['quarter'] == quarter]

    return df.to_dict(orient="records")
@router.get("/brands")
def get_top_mobile_brands():
    df = pd.read_csv("exports/transformed/aggregated_user.csv")

    # Check if columns exist to avoid runtime errors
    if "brand" not in df.columns or "count" not in df.columns:
        return {"error": "brand or count column not found in CSV"}

    top_brands = (
        df.groupby("brand", as_index=False)["count"].sum()
        .sort_values(by="count", ascending=False)
        .head(10)
    )
    return top_brands.to_dict(orient="records")

