from fastapi import Depends, FastAPI
from pydantic import BaseModel
from middlewares.auth import auth
from controllers import ocrGoogleVision, extractData

app = FastAPI()


class reqModel(BaseModel):
    image: str


@app.get("/")
async def root():
    return {"message": "Welcome! Access /docs to view api documentation"}


@app.post("/ocr-data", dependencies=[Depends(auth)])
async def ocrData(req: reqModel):
    ocrResult = ocrGoogleVision.ocrGoogleVisionApi(req.image)
    response = extractData.extractData(ocrResult)

    return response
