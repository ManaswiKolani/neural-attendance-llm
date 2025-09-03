from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from ..db import Base

class Cohort(Base):
    __tablename__ = "cohorts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)                 # e.g., "CS301 Fall 2025" or "West Team A"
    code = Column(String, nullable=True, unique=True)     # e.g., "CS301-F25"
    owner_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    settings = Column(JSON, nullable=True)                # optional: {"timezone":"America/Chicago","meeting_days":["Mon","Wed"]}

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
