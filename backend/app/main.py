import sys
print("Python path:", sys.path)
print("Starting FastAPI application...")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

print("Imported FastAPI successfully")

app = FastAPI(title="Healthcare Chatbot API", debug=True)
print("Created FastAPI app")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("Added CORS middleware")

@app.get("/health")
async def health_check():
    print("Health check endpoint called")
    return {"status": "healthy"}

print("Application setup complete")
