# app/models/person.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)

    cohort_id = Column(Integer, ForeignKey("cohorts.id"), nullable=True, index=True)

    name = Column(String, nullable=False)
    role = Column(String, nullable=True)           # e.g., "student", "employee"
    email = Column(String, nullable=True)
    external_id = Column(String, nullable=True)    # campus/work ID, badge number, etc.

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    embeddings = relationship("FaceEmbedding", back_populates="person", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_persons_cohort_name", "cohort_id", "name"),
        Index("ix_persons_cohort_external", "cohort_id", "external_id"),
    )
