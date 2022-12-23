"""Added first table 1

Revision ID: bc39c2aeb08d
Revises: cae5d111eed7
Create Date: 2022-12-23 13:19:57.295927

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'bc39c2aeb08d'
down_revision = 'cae5d111eed7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###