from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON, Index, Float
from sqlalchemy.sql import func
from ..db import Base

class RagAnswer(Base):
    __tablename__ = "rag_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    cohort_id = Column(Integer, ForeignKey("cohorts.id"), nullable=True, index=True)

    query_text = Column(Text, nullable=False)
    answer_text = Column(Text, nullable=False)
    strategy = Column(String, nullable=False)            # "sql_only" | "rag_only" | "hybrid" | "refusal_*"
    sql_snapshot = Column(JSON, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_rag_answers_created", "created_at"),
    )

class AnswerCitation(Base):
    __tablename__ = "answer_citations"

    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey("rag_answers.id"), nullable=False, index=True)
    source_doc_id = Column(Integer, ForeignKey("source_docs.id"), nullable=True, index=True)
    score = Column(Float, nullable=True)                  # retrieval similarity (optional)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_answer_citations_answer", "answer_id"),
    )
