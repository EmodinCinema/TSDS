"""empty message

Revision ID: first_data
Revises: 3861dc71f7b1
Create Date: 2022-11-30 15:45:06.663060

"""
from alembic import op
from sqlalchemy import orm
from src.models import User, Item
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '3861dc71f7b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    ivanov = User(email='ivanov@mail.ru', hashed_password='qwerty')
    petrov = User(email='petrov@mail.ru', hashed_password='asdfgh')

    session.add([ivanov, petrov])
    session.flush()

    book_harry = Item(title='Harry Potter', description='Book', owner_id=ivanov.id)
    book_rings = Item(title='The Lord of The Rings', description='Book', owner_id=ivanov.id)
    doka = Item(title='Dota 2', description='Game', owner_id=petrov.id)
    game = Item(title='Half Life 3', description='Game', owner_id=petrov.id)

    session.add([book_harry, book_rings, doka, game])
    session.commit()


def downgrade() -> None:
    pass


def downgrade() -> None:
    pass
