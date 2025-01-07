import uvicorn
from fastapi import FastAPI

print("Creating FastAPI app...")
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
