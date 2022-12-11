"""empty message

Revision ID: first_data
Revises: 0c509818b90d
Create Date: 2022-12-09 20:16:15.470387

"""
from alembic import op
from sqlalchemy import orm
import sqlalchemy as sa

from src.models import Recipient, Subscription, Edition


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '0c509818b90d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    alexandr = Recipient(name='Alexandr', surname='Grabovskij', patronymic='Sergeevich',
                       recipient_code='125', outside='Engels', house_number='1',
                       apartment_number='20')
    arsenty = Recipient(name='Arsenty', surname='Marco', patronymic='Sergeevich',
                       recipient_code='126', outside='Engels', house_number='7',
                       apartment_number='3')

    pravda = Edition(titles_of_the_publication='Pravda', index_of_the_publication=49848597,
                     type_of_publication='Newspaper', the_cost_of_searches_in_months=200)
    igromania = Edition(titles_of_the_publication='Igromania', index_of_the_publication=77969885,
                        type_of_publication='Magazine', the_cost_of_searches_in_months=346.99)

    session.add_all([alexandr, arsenty, pravda, igromania])
    session.flush()

    subscriptions_pravda = Subscription(subscription_period=8, month_of_delivery_start=2,
                                 year_of_delivery_start=2022,
                                 recipient_id=alexandr.id,
                                 edition_id=pravda.id)
    subscriptions_igromania = Subscription(subscription_period=5, month_of_delivery_start=6,
                                 year_of_delivery_start=2022,
                                 recipient_id=arsenty.id,
                                 edition_id=igromania.id)

    session.add_all([subscriptions_pravda, subscriptions_igromania])
    session.commit()


def downgrade() -> None:
    pass