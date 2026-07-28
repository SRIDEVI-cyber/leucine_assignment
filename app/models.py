from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")