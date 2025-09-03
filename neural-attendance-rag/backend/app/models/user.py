from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=True)            # e.g., "professor", "manager", "admin"

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
