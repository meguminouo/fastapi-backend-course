"""status

Revision ID: 11f4b61f7e45
Revises: 42ce89c43cea
Create Date: 2024-12-19 14:52:53.315454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11f4b61f7e45'
down_revision: Union[str, None] = '42ce89c43cea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', 'DELETED', name='userstatus'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###