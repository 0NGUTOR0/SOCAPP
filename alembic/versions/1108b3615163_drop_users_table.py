"""drop users table

Revision ID: 1108b3615163
Revises: 3f1e1b22526d
Create Date: 2024-03-14 19:05:47.793153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1108b3615163'
down_revision: Union[str, None] = '3f1e1b22526d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('users')
    pass


def downgrade() -> None:
    pass
