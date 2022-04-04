"""Comments

Revision ID: 24009c278a59
Revises: e00d66e35b01
Create Date: 2022-04-04 00:46:08.043564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24009c278a59'
down_revision = 'e00d66e35b01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_id', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    op.create_index('ix_post_id', 'post', ['id'], unique=False)
    # ### end Alembic commands ###
