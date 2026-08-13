from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.models.base import Base
from backend.app.models import *
from sqlalchemy import text

engine = create_engine(
    settings.database_url,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



def create_tables():
    with engine.connect() as conn:
        print(
            "Current database:",
            conn.execute(text("SELECT current_database()")).scalar(),
        )
        print(
            "Current schema:",
            conn.execute(text("SELECT current_schema()")).scalar(),
        )

    Base.metadata.create_all(bind=engine)

