from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, JSON, UniqueConstraint, Index
from sqlalchemy.sql import func
from ..db import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey("persons.id"), nullable=False, index=True)
    session_id = Column(Integer, ForeignKey("class_sessions.id"), nullable=False, index=True)

    status = Column(String, nullable=False, default="present")  # "present" | "absent" | "excused" | "late"
    recorded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    origin = Column(String, nullable=False, default="nn_autodetect")  # "nn_autodetect" | "manual" | "import"
    confidence = Column(Float, nullable=True)  # recognition confidence (0..1) when origin=nn_autodetect
    evidence = Column(JSON, nullable=True)  # e.g., {"model_version": "nn_v1", "frame_id": "abc", "notes": "..."}

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("person_id", "session_id", name="uix_person_session"),
        Index("ix_attendance_session_person", "session_id", "person_id"),
    )
