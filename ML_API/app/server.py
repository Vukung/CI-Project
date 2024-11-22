from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model
model = joblib.load('app/model.joblib')

# Initialize FastAPI app
app = FastAPI()

# Serve static files (e.g., CSS, JavaScript, or HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML form at the root URL
@app.get("/", response_class=HTMLResponse)
def read_form():
    with open("app/form.html", "r") as file:
        return HTMLResponse(content=file.read())

# Define a Pydantic model for request validation
class CustomInput(BaseModel):
    availability: int
    total_sqft: float
    bath: float
    balcony: float
    BHK: float
    area_type_Carpet_Area: bool  # Boolean field for Carpet Area
    area_type_Plot_Area: bool    # Boolean field for Plot Area
    area_type_Super_built_up_Area: bool  # Boolean field for Super built-up Area

# Predict function to handle form submission
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    availability: int = Form(...),
    total_sqft: float = Form(...),
    bath: float = Form(...),
    balcony: float = Form(...),
    BHK: float = Form(...),
    area_type: str = Form(...),
):
    """
    Predicts the house price based on the provided input features from the form.
    """
    # Convert area_type to one-hot encoding
    area_type_values = {
        "Carpet Area": [1, 0, 0],
        "Plot Area": [0, 1, 0],
        "Super built-up Area": [0, 0, 1],
    }

    area_type_encoded = area_type_values.get(area_type, [0, 0, 0])

    # Features for prediction
    features = [
        availability,
        total_sqft,
        bath,
        balcony,
        BHK,
        *area_type_encoded,
    ]

    # Make the prediction using the model
    prediction = model.predict([features])

    # Return the predicted price in HTML format
    return f"""
        <html>
            <body>
                <h2>Predicted House Price: ₹{prediction[0]:.2f}</h2>
                <a href="/">Go back</a>
            </body>
        </html>
    """

# Root endpoint to provide API info
@app.get('/api-info')
def read_root():
    return {'message': 'House price prediction model API'}
