from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Pet", back_populates="owner")


class Pet(database.Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    genus = Column(String, nullable=False)
    name = Column(String, nullable=True)
    extra_info = Column(String, nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")


class Spider(Pet):
    molt = Column(Integer, nullable=True)
    size = Column(Float, nullable=True)
    sex = Column(String, nullable=False, default="n")
