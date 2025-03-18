import os 

import mlflow.pyfunc
import pandas as pd

from pydantic import BaseModel
from fastapi import FastAPI

tag_metadata = [
    {
        "name": "Test Endpoint",
        "description": "LOREM IPSUM NEC."
    },

    {
        "name": "Test Endpoint",
        "description": "LOREM IPSUM NEC."
    }
]

app = FastAPI(
    title='GetAround API',
    description= """
    This API provides the model for price prediction for the GetAround Project
    """,
    version="1.0"
)

class RawData(BaseModel):
    input: list

class GetAroundUserForm(BaseModel):
    model_key: str = 'BMW'
    mileage: int = 100000
    engine_power: int = 135
    fuel:str = 'diesel'
    paint_color: str = 'black'
    car_type : str = 'estate'
    private_parking_available: bool = False
    has_gps: bool = True
    has_air_conditioning: bool = True
    automatic_car: bool = False
    has_getaround_connect: bool = False
    has_speed_regulator: bool = True
    winter_tires: bool = True

@app.on_event("startup")
async def app_startup():
    global model

    mlflow.set_tracking_uri(os.environ.get('MLFLOW_APP_URI'))
    model_name = 'get-around-model'
    model_alias = 'production'
    model = mlflow.pyfunc.load_model(f"models:/{model_name}@{model_alias}")
    print("Model from MLFlow server loaded successfully")


@app.get("/", tags=['Test Endpoint'])
async def index():
    
    """
    Return a test message.
    """

    message = "Hello world! This is the default endpoint. It means that the API server is up and everythings works."

    return message

@app.post('/predict', tags=['Predict Endpoint'])
async def predict_price(userform: GetAroundUserForm):
    
    """
    Return a price prediction. 
        
    """
    
    new_data = pd.DataFrame([{
        'model_key': userform.model_key,
        'mileage': userform.mileage,
        'engine_power': userform.engine_power,
        'fuel': userform.fuel,
        'paint_color': userform.paint_color,
        'car_type': userform.car_type,
        'private_parking_available': userform.private_parking_available,
        'has_gps': userform.has_gps,
        'has_air_conditioning': userform.has_air_conditioning,
        'automatic_car': userform.automatic_car,
        'has_getaround_connect': userform.has_getaround_connect,
        'has_speed_regulator': userform.has_speed_regulator,
        'winter_tires': userform.winter_tires
    }])
    
    for column in new_data.columns:
        if pd.api.types.is_numeric_dtype(new_data[column]):
            new_data[column] = new_data[column].astype(float)

    # Predict on a Pandas DataFrame.
    prediction = model.predict(new_data)
    
    return {"prediction": prediction.tolist()[0]}