from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from datetime import datetime

# Get the path to the
project_root = os.path.abspath(os.path.dirname(__file__))
db_file_path = os.path.join(project_root, 'sqlite3.db')

# Create your own engine here.  We'll use SQLite for ease.
engine = create_engine('sqlite:////%s' % db_file_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create our model Base. We will create models abstracting this base and it will be awesome.
Base = declarative_base()
Base.query = db_session.query_property()
# Alternatively, we could use the


# Build our models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)

    # We are going to have Facebook connect
    fb_id = Column(String)

    # When they signed up
    created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, email, name, fb_id):
        self.email = email
        self.name = name
        self.fb_id = fb_id


def init_db():

    Base.metadata.create_all(bind=engine)
