import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

AUTH_KEY = os.getenv("AUTH_KEY")


def auth(key: str = Header(...)):
    if key != AUTH_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida")
