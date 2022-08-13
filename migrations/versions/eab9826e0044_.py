"""empty message

Revision ID: eab9826e0044
Revises: d3d845b92d1a
Create Date: 2022-08-11 21:59:19.542962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab9826e0044'
down_revision = 'd3d845b92d1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shows_venue_id_fkey', 'shows', type_='foreignkey')
    op.drop_constraint('shows_artist_id_fkey', 'shows', type_='foreignkey')
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.create_foreign_key('shows_artist_id_fkey', 'shows', 'artists', ['artist_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('shows_venue_id_fkey', 'shows', 'venues', ['venue_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
