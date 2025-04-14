"""add password hash

Revision ID: 55f0c6efb293
Revises: 3c383004f438
Create Date: 2025-04-10 12:59:56.193279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '55f0c6efb293'
down_revision: Union[str, None] = '3c383004f438'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('password_hash, sqlmodel.sql.sqltypes.AutoString(), nullable = False'))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'password_hash')
