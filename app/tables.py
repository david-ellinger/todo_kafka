from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from faker import Faker
import click

from sqlalchemy.sql.sqltypes import DateTime
import logging
fake = Faker()

Base = declarative_base()
url = "sqlite:///todo.db"
engine = create_engine(url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class TodoTxt(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    completed = Column(Boolean, default=False)
    priority = Column(String, nullable=True)
    description = Column(String)
    completion_date = Column(DateTime, nullable=True)
    creation_date = Column(DateTime, default=datetime.now())
    project_tags = Column(String, nullable=True)  # TODO: Make this into its own table
    context_tags = Column(String, nullable=True)
    special_tags = Column(String, nullable=True)

def populate_database(users:int=5, todos:int=5):
    click.echo("Starting populate database")
    Base.metadata.create_all(bind=engine)
    session = scoped_session(Session)
    for _ in range(5):
        user = User(name=fake.name(), age=fake.random_int(18, 100))
        session.add(user)
    for _ in range(todos):
        task = TodoTxt(
            completed=fake.boolean(),
            priority=fake.random_uppercase_letter(),
            completion_date=datetime.now(),
            creation_date=datetime.now(),
            description=fake.sentence(),
            project_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
            context_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
            special_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
        )
        session.add(task)
    session.commit()
    click.echo("Finished populate database")

def drop():
    Base.metadata.drop_all(bind=engine)
