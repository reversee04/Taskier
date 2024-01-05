"""second upgrade

Revision ID: 39625ad531b7
Revises: d85101779a5b
Create Date: 2024-01-03 16:20:35.209081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39625ad531b7'
down_revision = 'd85101779a5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('to', sa.String(length=100), nullable=False),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('body', sa.String(length=1000000), nullable=False),
    sa.Column('attachment', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    op.drop_table('email')
    # ### end Alembic commands ###
