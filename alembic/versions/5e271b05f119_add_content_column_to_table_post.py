"""add content column to table post

Revision ID: 5e271b05f119
Revises: f1e8a7470845
Create Date: 2025-04-29 10:53:57.086479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e271b05f119'
down_revision: Union[str, None] = 'f1e8a7470845'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column( 'content',sa.String(), nullable=False ))
    


def downgrade() -> None:
    op.drop_column("posts","content")
    
