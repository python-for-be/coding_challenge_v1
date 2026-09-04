"""create_addresses_table

Revision ID: dfa44034202e
Revises: 952a814d2a70
Create Date: 2026-09-04 17:16:57.393311

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dfa44034202e"
down_revision: Union[str, Sequence[str], None] = "952a814d2a70"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "addresses",
        sa.Column("user_id", sa.Integer, nullable=False, primary_key=True),
        sa.Column("number", sa.String(10), nullable=False),
        sa.Column("street_name", sa.String(100), nullable=False),
        sa.Column("postcode", sa.String(20), nullable=False),
        sa.Column("city", sa.String(100), nullable=False),
        sa.Column("country", sa.String(100), nullable=False),
        sa.ForeignKeyConstraint(
            columns=["user_id"], refcolumns=["users.id"], name="fk_addresses_user_id", ondelete="CASCADE"
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("addresses")
