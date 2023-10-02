"""empty message

Revision ID: 10e23ffaa6c0
Revises: ecdcb0212975
Create Date: 2023-10-02 13:12:28.211212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10e23ffaa6c0'
down_revision = 'ecdcb0212975'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vyrobce',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vyrobce')
    # ### end Alembic commands ###
