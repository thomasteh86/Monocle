"""Added ix_coords_sp to spawnpoints

Revision ID: 32aede9e7e69
Revises: f19fc04ba856
Create Date: 2017-09-24 03:14:44.748056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32aede9e7e69'
down_revision = 'f19fc04ba856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_coords_sp', 'spawnpoints', ['lat', 'lon'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_coords_sp', table_name='spawnpoints')
    # ### end Alembic commands ###
