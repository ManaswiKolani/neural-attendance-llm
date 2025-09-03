from sqlalchemy import Column, Integer, LargeBinary, ForeignKey, String, DateTime, Float, JSON, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db import Base

class FaceEmbedding(Base):
    __tablename__ = "face_embeddings"

    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey("persons.id"), nullable=False, index=True)

    vector = Column(LargeBinary, nullable=False)          # np.float32 bytes
    embedding_dim = Column(Integer, nullable=False, default=128)
    model_version = Column(String, nullable=False, default="nn_v1")

    origin = Column(String, nullable=False, default="enroll")   # "enroll" | "refresh" | "import"
    quality = Column(Float, nullable=True)                      # optional face/embedding quality score
    extra = Column(JSON, nullable=True)                         # e.g., {"align":"mtcnn","crop_size":128}

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    person = relationship("Person", back_populates="embeddings")

    __table_args__ = (
        Index("ix_face_embeddings_model_version", "model_version"),
    )
