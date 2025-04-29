"""create posts table

Revision ID: 51c3c8d7bad1
Revises: 
Create Date: 2025-04-29 09:07:15.586043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51c3c8d7bad1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.INTEGER(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))    
    


def downgrade() -> None:
    op.drop_table("posts")
    
