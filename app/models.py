from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(500))
    status = Column(String(50))