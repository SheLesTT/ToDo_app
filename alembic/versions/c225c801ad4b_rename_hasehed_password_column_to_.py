"""rename hasehed_password column to password

Revision ID: c225c801ad4b
Revises: 49b66aee4235
Create Date: 2023-08-15 09:42:37.599582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c225c801ad4b'
down_revision: Union[str, None] = '49b66aee4235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'hashed_password', new_column_name='password')
    pass


def downgrade() -> None:
    pass
