"""Create_phone_number_for_user_column

Revision ID: 46b96570050a
Revises: 
Create Date: 2025-03-11 16:59:42.557777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b96570050a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable= True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users','phone_number')
