"""empty message

Revision ID: 115366927ec4
Revises: 79ab104337fe
Create Date: 2018-07-12 21:53:32.817136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115366927ec4'
down_revision = '79ab104337fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('introduction', sa.Text(), nullable=True))
    op.add_column('posts', sa.Column('subtitle', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'subtitle')
    op.drop_column('posts', 'introduction')
    # ### end Alembic commands ###