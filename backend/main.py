from fastapi import FastAPI
from control import volume, brightness, trackpad
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/volume/set/{level}")
def set_volume(level: int):
    volume.set_volume(level)
    return {"status": "success", "volume": level}

@app.post("/volume/increase")
def increase_volume():
    volume.increase_volume()
    return {"status": "success"}

@app.post("/brightness/increase")
def increase_brightness():
    brightness.increase_brightness()
    return {"status": "success"}

@app.post("/brightness/decrease")
def decrease_brightness():
    brightness.decrease_brightness()
    return {"status": "success"}

@app.post("/mouse/move")
def move_mouse(x: float, y: float):
    trackpad.move_mouse(x, y)
    return {"status": "success", "x": x, "y": y}

@app.post("/mouse/click")
def click_mouse(x: float, y: float):
    trackpad.click_mouse(x, y)
    return {"status": "success", "x": x, "y": y}
