from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/transactions")
def get_map_transactions():
    df = pd.read_csv("exports/transformed/map_transaction.csv")
    return df.to_dict(orient="records")

@router.get("/users")
def get_map_users():
    df = pd.read_csv("exports/transformed/map_user.csv")
    return df.to_dict(orient="records")
