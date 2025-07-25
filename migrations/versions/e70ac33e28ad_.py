"""empty message

Revision ID: e70ac33e28ad
Revises: c5fc09634fbc
Create Date: 2025-07-11 21:30:46.151112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70ac33e28ad'
down_revision = 'c5fc09634fbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.drop_constraint('personajes_id_usuario_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'guardar', ['id_usuario'], ['id'])

    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.drop_constraint('planetas_id_usuario_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'guardar', ['id_usuario'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('planetas_id_usuario_fkey', 'usuario', ['id_usuario'], ['id'])

    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('personajes_id_usuario_fkey', 'usuario', ['id_usuario'], ['id'])

    # ### end Alembic commands ###
