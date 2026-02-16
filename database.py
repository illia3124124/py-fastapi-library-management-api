from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(
    "sqlite:///library.db"
)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=True,
    autoflush=True
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
