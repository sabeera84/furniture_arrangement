from fastapi import FastAPI
from pydantic import BaseModel
from dataset_opt import genetic_algorithm

# Initialize FastAPI app
app = FastAPI()

# Define request model
class RoomInput(BaseModel):
    width: int
    height: int
    num_furniture: int

# API endpoint to get optimized furniture layout
@app.post("/optimize")
def optimize_layout(room: RoomInput):
    optimized_layout = genetic_algorithm((room.width, room.height), room.num_furniture)
    return {"layout": optimized_layout}

# Run using: uvicorn app:app --reload
