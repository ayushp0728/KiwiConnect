# 📱💻 Mac Remote Control via FastAPI

This project allows you to **control your MacBook remotely using your phone** (or any other device) through simple API endpoints.  
You can adjust **volume**, **brightness**, and even **move or click the mouse** — all from your smartphone’s browser or a simple frontend interface.

---

## 🚀 Overview

The backend is built with **FastAPI**, a lightweight and high-performance Python web framework.  
It exposes RESTful endpoints that communicate with local Python scripts (`volume.py`, `brightness.py`, and `trackpad.py`) which execute system-level commands on macOS.

With this, your phone becomes a remote for your MacBook — useful for things like:
- Adjusting volume from a distance  
- Dimming or increasing brightness  
- Moving the mouse or performing clicks remotely  

---

## 🧠 How It Works

1. The **FastAPI server** runs locally on your MacBook.  
2. Your **phone connects to the same Wi-Fi network** and sends HTTP requests to the FastAPI endpoints.  
3. Each endpoint triggers a corresponding function in `volume.py`, `brightness.py`, or `trackpad.py`, which executes system commands using macOS libraries (like `osascript` or `pyobjc`).  

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
Make sure you have Python 3.9+ installed. Then install the required dependencies:
```bash
pip install fastapi uvicorn
