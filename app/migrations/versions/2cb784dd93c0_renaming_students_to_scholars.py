"""Renaming students to scholars

Revision ID: 2cb784dd93c0
Revises: 8001ce3060c2
Create Date: 2025-05-22 10:58:00.054260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb784dd93c0'
down_revision = '8001ce3060c2'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('students', 'scholars')


def downgrade():
    op.rename_table('scholars', 'students')
