"""fix: ForeignKey for ClientModel

Revision ID: d25a7edd3aea
Revises: 7873949ecbc6
Create Date: 2022-05-03 11:00:36.015940

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d25a7edd3aea"
down_revision = "7873949ecbc6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("products_name_key", "products", type_="unique")
    op.drop_constraint("sales_client_id_key", "sales", type_="unique")
    op.drop_constraint("sales_payment_id_key", "sales", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("sales_payment_id_key", "sales", ["payment_id"])
    op.create_unique_constraint("sales_client_id_key", "sales", ["client_id"])
    op.create_unique_constraint("products_name_key", "products", ["name"])
    # ### end Alembic commands ###