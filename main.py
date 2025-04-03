from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Base, engine
from crud import add_camera, add_anomaly

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define FastAPI app instance
app = FastAPI()

@app.get("/scan")
def get_scan_results(db: Session = Depends(get_db)):
    scanned_cameras = scan_network()  # Ensure this function is defined
    for camera in scanned_cameras:
        add_camera(db, camera["ip_address"], camera["hostname"], ",".join(camera["open_ports"].keys()))
    return {"cameras": scanned_cameras}

@app.post("/detect")
def detect_anomaly(data: dict, db: Session = Depends(get_db)):
    result = detect_anomalies(data)  # Ensure this function is defined
    if result == "Anomaly":
        add_anomaly(db, data["src_ip"], "Suspicious Activity")
    return {"status": result}  # Fixed syntax error
