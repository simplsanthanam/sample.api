"""add last few column to table posts

Revision ID: 55a35bfe28e4
Revises: 840ceae90090
Create Date: 2025-04-29 12:02:29.207828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55a35bfe28e4'
down_revision: Union[str, None] = '840ceae90090'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    


def downgrade() -> None:
      op.drop_column("posts", "published")
      op.drop_column("posts", "created_at")
      
      
