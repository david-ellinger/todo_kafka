from datetime import datetime
from dotenv import load_dotenv
import click
from sqlalchemy.sql.sqltypes import DateTime, STRINGTYPE
from todoist_service import TodoistService
import sqlite3
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()  # take env variables from .env

Base = declarative_base()


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


url = "sqlite:///todo.db"
engine = create_engine(url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


@click.group()
def cli():
    pass

@cli.command()
def add(description:str):
    task = TodoTxt(description=description)
    print(f"Task: {task}")

@cli.command()
def sync():
    todoist = TodoistService()
    todoist.sync()


@cli.command()
@click.option("--todos", default=5, help="Number todo rows")
def initdb(todos):
    # TODO: Initialize sqlite db
    session = scoped_session(Session)
    fake = Faker()

    for _ in range(5):
        user = User(name=fake.name(), age=fake.random_int(18, 100))
        session.add(user)
    for _ in range(todos):
        task = TodoTxt(
            completed=fake.boolean(),
            priority=fake.random_uppercase_letter(),
            completion_date=fake.date(),
            creation_date=fake.date(),
            description=fake.sentence(),
            project_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
            context_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()},{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
            special_tags=f"{fake.random_uppercase_letter()}:{fake.random_uppercase_letter()}",
        )
        session.add(task)
    session.commit()
    click.echo("Initialized the database")


def add():

    pass


@cli.command()
def dropdb():
    # TODO: Drop sqlite db
    Base.metadata.drop_all(bind=engine)
    click.echo("Dropped the database")


if __name__ == "__main__":
    cli()
