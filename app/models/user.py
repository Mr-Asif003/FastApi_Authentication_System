from datetime import datetime
from enum import unique
from pickle import FALSE

from pydantic import BaseModel

from app.db.pg_db import Base
from sqlalchemy import String,Boolean,DateTime
from sqlalchemy.orm import Mapped,mapped_column

class User(Base):
    __tablename__ = "users"

    id:Mapped[int]=mapped_column(
        primary_key=True,
        index=True
    )
    name:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    hashed_password:Mapped[str]=mapped_column(
        String(50),
        nullable=False
    )
    role:Mapped[bool]=mapped_column(
        String(50),
        nullable=False,
        default='user'
    )
    is_active:Mapped[bool]=mapped_column(
        Boolean,
        default=True
    )
    createdAt:Mapped[bool]=mapped_column(
        DateTime,
        default=datetime.utcnow(),
        nullable=False
    )
