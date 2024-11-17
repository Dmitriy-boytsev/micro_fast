from sqlalchemy import Column, String, Date

from app.core.db import Base


class Clients(Base):
    name = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), unique=True, nullable=False)
    date = Column(Date, unique=True, nullable=False)


class RegularClients(Base):
    name = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), unique=True, nullable=False)
    date = Column(Date, unique=True, nullable=False)
