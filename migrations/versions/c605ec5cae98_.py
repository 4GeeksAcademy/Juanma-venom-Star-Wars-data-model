"""empty message

Revision ID: c605ec5cae98
Revises: 3af8879c7a46
Create Date: 2025-07-11 21:22:31.850133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c605ec5cae98'
down_revision = '3af8879c7a46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_personajes', sa.Integer(), nullable=True))
        batch_op.drop_constraint('personajes_personajes_key', type_='unique')
        batch_op.drop_constraint('personajes_id_usuario_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'personajes', ['id_personajes'], ['id'])
        batch_op.drop_column('id_usuario')
        batch_op.drop_column('personajes')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('personajes', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('id_usuario', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('personajes_id_usuario_fkey', 'usuario', ['id_usuario'], ['id'])
        batch_op.create_unique_constraint('personajes_personajes_key', ['personajes'])
        batch_op.drop_column('id_personajes')

    # ### end Alembic commands ###
