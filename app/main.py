from fastapi import FastAPI
from src.predict import predict_traffic

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Traffic Optimization Model Running"}

@app.post("/predict")
def predict(day:int,
            hour:int,
            festival:int,
            rain:int,
            weather:int,
            vehicle_count:int):

    features = [
        day,
        hour,
        festival,
        rain,
        weather,
        vehicle_count
    ]

    result = predict_traffic(features)

    return result