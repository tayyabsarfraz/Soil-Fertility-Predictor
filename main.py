from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Mount static files (for background image)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Load trained GBM model
gbm_model = joblib.load("gbm_model.pkl")

# Map numeric predictions to text
fertility_map = {0: "Low", 1: "Medium", 2: "High"}

# -------------------------------
# Home page with form
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": ""})

# -------------------------------
# Prediction route
# -------------------------------
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    nitrogen: float = Form(...),
    phosphorous: float = Form(...),
    potassium: float = Form(...)
):
    # Prepare input
    X_new = np.array([[nitrogen, phosphorous, potassium]])
    
    # Predict
    pred_class = gbm_model.predict(X_new)[0]
    result = fertility_map.get(pred_class, "Unknown")
    
    # Return result
    return templates.TemplateResponse("index.html", {"request": request, "prediction": result})
