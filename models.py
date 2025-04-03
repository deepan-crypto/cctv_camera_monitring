from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime

class Camera(Base):
    __tablename__ = "cameras"  # Corrected typo

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, unique=True, index=True)
    hostname = Column(String)
    open_ports = Column(String)
    last_seen = Column(DateTime, default=datetime.datetime.utcnow)

class Anomaly(Base):
    __tablename__ = "anomalies"  # Corrected typo

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, index=True)
    alert_type = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = "users"  # Corrected typo

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
