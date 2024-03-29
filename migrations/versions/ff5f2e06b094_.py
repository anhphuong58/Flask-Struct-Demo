"""empty message

Revision ID: ff5f2e06b094
Revises: 
Create Date: 2023-03-01 14:55:36.871777

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'ff5f2e06b094'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=300), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('role', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('campaign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bid_amount', sa.Integer(), nullable=True),
    sa.Column('used_amount', sa.Integer(), nullable=True),
    sa.Column('usage_rate', sa.Float(), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('final_url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('preview', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign')
    op.drop_table('user')
    # ### end Alembic commands ###
