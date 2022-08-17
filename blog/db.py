from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./blog/blog.db',
                       connect_args={"check_same_thread": False}, echo=True)

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


def getdata_base():
    data_base = SessionLocal()
    try:
        yield data_base
    finally:
        data_base.close()