"""add name column to users table

Revision ID: 3f1e1b22526d
Revises: 37d6a2e5ee5f
Create Date: 2024-03-14 18:54:24.719519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f1e1b22526d'
down_revision: Union[str, None] = '37d6a2e5ee5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("name", sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('users', "name")
    pass

