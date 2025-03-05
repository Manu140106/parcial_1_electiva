from fastapi import FastAPI

app = FastAPI()

@app.get("/info")  
def get_info():
    return {
        "name": "GastroBot",
        "version": "1.0",
        "description": "A recipe assistant API",
        "author": "Paula",
        "status": "active"
    }