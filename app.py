from datetime import datetime

from sqlalchemy.orm.scoping import scoped_session
from app.tables import Base, Session, TodoTxt, User, drop, engine, populate_database
from app.todoist_service import TodoistService
from dotenv import load_dotenv
import click


load_dotenv()  # take env variables from .env


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
    populate_database()
    click.echo("Initialized the database")


def add():
    pass


@cli.command()
def dropdb():
    drop()
    click.echo("Dropped the database")

if __name__ == "__main__":
    cli()
