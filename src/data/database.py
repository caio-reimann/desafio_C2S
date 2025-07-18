import os
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine: Engine = create_engine(os.getenv("DB_URL", default="sqlite:///cars.db"))
session: Session = Session(engine)
