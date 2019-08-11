from os import getenv
from sqlalchemy import create_engine
from sqlalchan.example import Model

# define your DB here, I use PostgreSQL and this expect define of USER, PASSWORD and DB name in environment variables
# DB_USER, DB_PASS and DB
engine = create_engine(f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASS')}@postgres/{getenv('DB')}")

Model.metadata.create_all(engine)
