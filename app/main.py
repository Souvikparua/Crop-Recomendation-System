from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from app.model import CropRecommendationModel

app = FastAPI()

model = CropRecommendationModel()

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.post("/recommend")
async def recommend_crop(input: CropInput):
    features = {
        "N": input.N,
        "P": input.P,
        "K": input.K,
        "temperature": input.temperature,
        "humidity": input.humidity,
        "ph": input.ph,
        "rainfall": input.rainfall
    }
    
    try:
        recommended_crop = model.recommend_crop(features)
        return {"recommended_crop": recommended_crop}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

