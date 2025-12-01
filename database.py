from sqlalchemy import (create_engine, Column, INTEGER, String,
                        TEXT, NUMERIC, and_, or_, between)
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:1@localhost:5432/postgres",
                       echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()

class User(Base):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    photo = Column(String)
    name = Column(String)
    age = Column(INTEGER)
    address = Column(String)



Base.metadata.create_all(engine)