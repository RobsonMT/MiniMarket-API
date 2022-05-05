"""fix: cliente default values and nullable to False. Product ,productCategories and categories rules.

Revision ID: 659011afb05d
Revises: ecbfbae4e149
Create Date: 2022-04-30 18:25:57.787265

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "659011afb05d"
down_revision = "ecbfbae4e149"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "categories", "name", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.create_unique_constraint(None, "categories", ["name"])
    op.add_column(
        "clients", sa.Column("establishment_id", sa.Integer(), nullable=False)
    )
    op.alter_column("clients", "name", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("clients", "contact", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("clients", "pay_day", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("clients", "is_dobtor", existing_type=sa.BOOLEAN(), nullable=False)
    op.alter_column("clients", "is_late", existing_type=sa.BOOLEAN(), nullable=False)
    op.alter_column(
        "clients", "is_activate", existing_type=sa.BOOLEAN(), nullable=False
    )
    op.create_unique_constraint(None, "clients", ["establishment_id"])
    op.drop_constraint("clients_estabilishment_id_fkey", "clients", type_="foreignkey")
    op.create_foreign_key(
        None, "clients", "establishments", ["establishment_id"], ["id"]
    )
    op.drop_column("clients", "estabilishment_id")
    op.alter_column(
        "product_categories", "product_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.alter_column(
        "product_categories", "category_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.alter_column(
        "products", "name", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.alter_column(
        "products", "sale_price", existing_type=sa.NUMERIC(), nullable=False
    )
    op.alter_column(
        "products", "cost_price", existing_type=sa.NUMERIC(), nullable=False
    )
    op.alter_column(
        "products", "unit_type", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.alter_column(
        "products", "establishment_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.create_unique_constraint(None, "products", ["name"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "products", type_="unique")
    op.alter_column(
        "products", "establishment_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.alter_column(
        "products", "unit_type", existing_type=sa.VARCHAR(length=100), nullable=True
    )
    op.alter_column("products", "cost_price", existing_type=sa.NUMERIC(), nullable=True)
    op.alter_column("products", "sale_price", existing_type=sa.NUMERIC(), nullable=True)
    op.alter_column(
        "products", "name", existing_type=sa.VARCHAR(length=100), nullable=True
    )
    op.alter_column(
        "product_categories", "category_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.alter_column(
        "product_categories", "product_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.add_column(
        "clients",
        sa.Column(
            "estabilishment_id", sa.INTEGER(), autoincrement=False, nullable=True
        ),
    )
    op.drop_constraint(None, "clients", type_="foreignkey")
    op.create_foreign_key(
        "clients_estabilishment_id_fkey",
        "clients",
        "establishments",
        ["estabilishment_id"],
        ["id"],
    )
    op.drop_constraint(None, "clients", type_="unique")
    op.alter_column("clients", "is_activate", existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column("clients", "is_late", existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column("clients", "is_dobtor", existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column("clients", "pay_day", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column("clients", "contact", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("clients", "name", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_column("clients", "establishment_id")
    op.drop_constraint(None, "categories", type_="unique")
    op.alter_column(
        "categories", "name", existing_type=sa.VARCHAR(length=100), nullable=True
    )
    # ### end Alembic commands ###
