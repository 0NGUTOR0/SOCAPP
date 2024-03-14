"""create users table

Revision ID: 37d6a2e5ee5f
Revises: 
Create Date: 2024-03-14 18:18:00.996956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37d6a2e5ee5f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                            sa.Column('email', sa.String, unique=True, nullable= False),
                            sa.Column('password', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
