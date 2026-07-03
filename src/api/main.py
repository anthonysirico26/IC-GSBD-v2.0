from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the API
app = FastAPI(title="Project JUNIOR Inference API")

# Define what the incoming data should look like
class InferenceRequest(BaseModel):
    feature_1: float
    feature_2: float

@app.get("/")
def health_check():
    return {"status": "healthy", "model_version": "v1.0.0"}

@app.post("/predict")
def predict(request: InferenceRequest):
    # TODO: Load your model from the models/ folder
    # model = load_model("models/best_model.pkl")
    # prediction = model.predict([[request.feature_1, request.feature_2]])
    
    return {
        "status": "success",
        "input_received": request.dict(),
        "prediction": "placeholder_result"
    }