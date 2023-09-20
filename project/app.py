import time

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post('/api')
def predict():
    time.sleep(0.5)
    return {"status": 200}

@app.post('/api2')
def predict():
    time.sleep(0.5)
    return {"status": 200}

@app.post('/api3')
def predict():
    time.sleep(0.5)
    return {"status": 200}

if __name__ == "__main__":
    uvicorn.run('app:app', workers=4, reload=True)