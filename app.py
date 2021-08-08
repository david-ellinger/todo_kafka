from dotenv import load_dotenv
import click
from todoist_service import TodoistService
import sqlite3
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
load_dotenv() # take env variables from .env

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

url = "sqlite:///todo.db"
engine = create_engine(url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def sync():
    todoist = TodoistService()
    todoist.sync()

# Examples / Test

@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@cli.command()
def initdb():
    #TODO: Initialize sqlite db
    session = scoped_session(Session)
    fake = Faker()

    for _ in range(1000):
        user = User(name=fake.name(), age=fake.random_int(18,100))
        session.add(user)
    session.commit()
    # t1 = Table('Table_1', meta,
    #         Column('id', Integer, primary_key=True),
    #         Column('name',String))
    # t2 = Table('Table_2', meta,
    #         Column('id', Integer, primary_key=True),
    #         Column('val',Integer))
    # t1.create()
    # t2.create()
    # conn = sqlite3.connect('test.db')
    # c = conn.cursor()
    # c.execute("CREATE TABLE todo (id varchar(3), data json)")
    click.echo('Initialized the database')

def add():
    pass

@cli.command()
def dropdb():
    #TODO: Drop sqlite db
    Base.metadata.drop_all(bind=engine)
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
