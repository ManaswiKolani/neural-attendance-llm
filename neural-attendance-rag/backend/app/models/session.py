from sqlalchemy import Column, Integer, Date, String, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.sql import func
from ..db import Base

class ClassSession(Base):
    __tablename__ = "class_sessions"

    id = Column(Integer, primary_key=True)
    cohort_id = Column(Integer, ForeignKey("cohorts.id"), nullable=False, index=True)
    date = Column(Date, nullable=False)
    topic = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("cohort_id", "date", name="uix_cohort_date"),
        Index("ix_sessions_cohort_date", "cohort_id", "date"),
    )
