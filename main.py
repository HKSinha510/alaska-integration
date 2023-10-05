import uvicorn
from fastapi import FastAPI
from fetch_system import allinfo

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/systeminfo")
def system_info():
    inst = allinfo()
    inst.group_values()
    return inst.stat

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)