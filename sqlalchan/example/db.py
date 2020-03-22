from os import getenv
from sqlalchemy import create_engine
# uncomment if you want to test it with insert
# from sqlalchemy.orm import Session
from sqlalchan.example.model import Model #, Country

# define your DB here, I use PostgreSQL and this expect define of USER, PASSWORD and DB name in environment variables
# DB_USER, DB_PASS and DB
engine = create_engine(f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASS')}@postgres_test:5433/{getenv('DB')}")

# create all tables
Model.metadata.create_all(engine)

# uncomment if you want to test insert

"""session = Session(bind=engine)
session.add(
    Country(
        name='China',
        code='CH'
    )
)
session.commit()"""

print("Hello! I'm running!")




