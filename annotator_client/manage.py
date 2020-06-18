import click
from flask.cli import FlaskGroup

from annotator_client.app import create_app


def create_annotator_client(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_annotator_client)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from annotator_client.extensions import db
    from annotator_client.models import User

    click.echo("create user")
    user = User(username="admin", email="admin@mail.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
