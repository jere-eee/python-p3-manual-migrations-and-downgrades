"""Renaming students to scholars

Revision ID: bb21b9d61100
Revises: 791279dd0760
Create Date: 2024-12-10 15:38:22.735591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb21b9d61100'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
