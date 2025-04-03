from sqlalchemy.orm import Session
from models import Camera, Anomaly, User
from passlib.hash import bcrypt

# Store scanned cameras
def add_camera(db: Session, ip, hostname, ports):
    camera = Camera(ip_address=ip, hostname=hostname, open_ports=ports)
    db.add(camera)
    db.commit()

# Store anomaly detection logs
def add_anomaly(db: Session, ip, alert_type):
    anomaly = Anomaly(ip_address=ip, alert_type=alert_type)
    db.add(anomaly)
    db.commit()

# Authenticate user
def authenticate_user(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt.verify(password, user.hashed_password):
        return user
    return None