from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    filename = Column(String, unique=True)
    upload_date = Column(DateTime, default=datetime.utcnow)

# Updated models including OCR text and tags
