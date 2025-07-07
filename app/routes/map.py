from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()

@router.get("/transactions")
def get_map_transactions(year: int = None, quarter: int = None):
    df = pd.read_csv("exports/transformed/map_transaction.csv")

    if year is not None:
        df = df[df["year"] == year]
    if quarter is not None:
        df = df[df["quarter"] == quarter]

    return df.to_dict(orient="records")

@router.get("/users")
def get_map_users(year: int = None, quarter: int = None):
    df = pd.read_csv("exports/transformed/map_user.csv")

    if year is not None:
        df = df[df["year"] == year]
    if quarter is not None:
        df = df[df["quarter"] == quarter]

    return df.to_dict(orient="records")
