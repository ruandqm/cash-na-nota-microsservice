from fastapi import Depends, FastAPI
from pydantic import BaseModel
from middlewares.auth import auth
from controllers import ocrGoogleVision, extractData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class reqModel(BaseModel):
    image: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome! Access /docs to view api documentation"}


@app.post("/ocr-data", dependencies=[Depends(auth)])
async def ocrData(req: reqModel):
    ocrResult = ocrGoogleVision.ocrGoogleVisionApi(req.image)
    response = extractData.extractData(ocrResult)

    return response
