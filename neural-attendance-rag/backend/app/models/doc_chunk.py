from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.sql import func
from ..db import Base

class DocChunk(Base):
    __tablename__ = "doc_chunks"

    id = Column(Integer, primary_key=True)

    source_doc_id = Column(Integer, ForeignKey("source_docs.id"), nullable=False, index=True)
    idx = Column(Integer, nullable=False)                 # chunk sequence within the source doc

    text = Column(Text, nullable=False)                   # extracted chunk text
    embedding = Column(LargeBinary, nullable=True)        # per-chunk vector (np.float32 bytes), optional

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("source_doc_id", "idx", name="uix_chunk_source_idx"),
        Index("ix_doc_chunks_source_idx", "source_doc_id", "idx"),
    )
