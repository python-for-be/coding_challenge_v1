"""create_users_table

Revision ID: 952a814d2a70
Revises:
Create Date: 2026-09-04 17:11:46.869024

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "952a814d2a70"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, nullable=False, primary_key=True, autoincrement=True),
        sa.Column("firstname", sa.String(100), nullable=False),
        sa.Column("lastname", sa.String(100), nullable=False),
        sa.Column("date_of_birth", sa.DATE, nullable=False),
    )


def downgrade():
    op.drop_table("users")
