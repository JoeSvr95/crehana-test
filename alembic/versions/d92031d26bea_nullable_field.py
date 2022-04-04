"""Nullable field

Revision ID: d92031d26bea
Revises: 0de887b88504
Create Date: 2022-04-04 00:58:14.883733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd92031d26bea'
down_revision = '0de887b88504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'postId',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'postId',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
