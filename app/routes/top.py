from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/transactions")
def get_top_transactions():
    df = pd.read_csv("exports/transformed/top_transaction.csv")
    return df.to_dict(orient="records")

@router.get("/users")
def get_top_users():
    df = pd.read_csv("exports/transformed/top_user.csv")
    return df.to_dict(orient="records")
