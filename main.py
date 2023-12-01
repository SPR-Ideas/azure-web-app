"""
    Description : An test application for Azure Web app .
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def health_check():
    """Returns Hello world"""
    return "hello world"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)