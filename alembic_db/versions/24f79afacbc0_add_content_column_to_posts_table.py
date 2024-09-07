"""add content column to posts table

Revision ID: 24f79afacbc0
Revises: 8ab3b0852dc9
Create Date: 2024-09-03 15:41:32.518908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24f79afacbc0'
down_revision: Union[str, None] = '8ab3b0852dc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
