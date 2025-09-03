from sqlalchemy import Column, Integer, String, Text, LargeBinary, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..db import Base

class SourceDoc(Base):
    __tablename__ = "source_docs"
    id = Column(Integer, primary_key=True)
    source_type = Column(String, nullable=False)   # "policy" | "schedule" | "note" | "email" | "syllabus" | "other"
    title = Column(String, nullable=False)
    uploader_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    cohort_id = Column(Integer, ForeignKey("cohorts.id"), nullable=True)  # scope visibility
    original_file_name = Column(String, nullable=True)
    mime_type = Column(String, nullable=True)
    size_bytes = Column(Integer, nullable=True)
    storage_path = Column(String, nullable=True)   # where the file lives (if stored)
    content = Column(Text, nullable=False)         # extracted text
    embedding = Column(LargeBinary, nullable=True) # optional whole-doc embedding
    metadata = Column(JSON, nullable=True)         # headers, dates, tags
    content_hash = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
            Index("ix_source_docs_type", "source_type"),
            Index("ix_source_docs_content_hash", "content_hash"),
        )