"""Create tables

Revision ID: 49b66aee4235
Revises: 
Create Date: 2023-08-14 13:04:44.903216

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49b66aee4235'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users', sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('name', sa.String)
    )
    op.create_table(
        'tasks', sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('content', sa.String, nullable=True),
        sa.Column('is_done', sa.Boolean, nullable=False, server_default='FALSE')
    )
    pass


def downgrade() -> None:
    pass
