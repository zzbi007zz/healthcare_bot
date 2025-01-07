from fastapi import FastAPI
import uvicorn
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    try:
        logger.info("Starting server...")
        uvicorn.run("minimal:app", host="127.0.0.1", port=8000, reload=True, access_log=True)
    except Exception as e:
        logger.error(f"Error starting server: {e}", exc_info=True)
