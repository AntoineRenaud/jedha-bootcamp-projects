import mlflow
import uvicorn
import pandas as pd
import numpy as np
import joblib
import boto3

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

logged_model = 's3://mlflowserver-bucket/1/858646db304b45b3bd4ab65c4670b5ec/artifacts/LinearRegression'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

class RawData(BaseModel):
    input: list

class GetAroundUserForm(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color :str
    car_type :str
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool

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
      
    preprocessor = joblib.load('preprocessor.pkl')
    new_data = preprocessor.transform(new_data)

    # Predict on a Pandas DataFrame.
    prediction = loaded_model.predict(new_data)
    
    return {"prediction": prediction.tolist()[0]}


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)