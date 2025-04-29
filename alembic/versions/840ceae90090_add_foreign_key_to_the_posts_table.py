"""add foreign key to the posts table

Revision ID: 840ceae90090
Revises: 5e271b05f119
Create Date: 2025-04-29 11:25:20.068075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '840ceae90090'
down_revision: Union[str, None] = '5e271b05f119'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.INTEGER(),nullable=False))
    op.create_foreign_key("post_user_fk",source_table="posts",referent_table="users",local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
    pass
