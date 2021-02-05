"""empty message

Revision ID: 7ad4f4e9edc8
Revises: 
Create Date: 2021-02-04 23:26:57.499850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ad4f4e9edc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sl_channels',
    sa.Column('id', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Unicode(length=250), nullable=True),
    sa.Column('archived_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sl_channels_archived_at'), 'sl_channels', ['archived_at'], unique=False)
    op.create_index(op.f('ix_sl_channels_name'), 'sl_channels', ['name'], unique=False)
    op.create_table('sl_users',
    sa.Column('id', sa.String(length=11), nullable=False),
    sa.Column('name', sa.Unicode(length=80), nullable=False),
    sa.Column('full_name', sa.Unicode(length=80), nullable=True),
    sa.Column('description', sa.Unicode(length=250), nullable=True),
    sa.Column('avatar_id', sa.String(length=16), nullable=True),
    sa.Column('tz_offset', sa.String(length=9), nullable=True),
    sa.Column('archived_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sl_users_archived_at'), 'sl_users', ['archived_at'], unique=False)
    op.create_index(op.f('ix_sl_users_name'), 'sl_users', ['name'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oa_id', sa.String(length=50), nullable=False),
    sa.Column('oa_provider', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_oa_id'), 'users', ['oa_id'], unique=False)
    op.create_index(op.f('ix_users_oa_provider'), 'users', ['oa_provider'], unique=False)
    op.create_table('apps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Unicode(length=255), nullable=True),
    sa.Column('token', sa.String(length=43), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apps_name'), 'apps', ['name'], unique=False)
    op.create_index(op.f('ix_apps_token'), 'apps', ['token'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_apps_token'), table_name='apps')
    op.drop_index(op.f('ix_apps_name'), table_name='apps')
    op.drop_table('apps')
    op.drop_index(op.f('ix_users_oa_provider'), table_name='users')
    op.drop_index(op.f('ix_users_oa_id'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_sl_users_name'), table_name='sl_users')
    op.drop_index(op.f('ix_sl_users_archived_at'), table_name='sl_users')
    op.drop_table('sl_users')
    op.drop_index(op.f('ix_sl_channels_name'), table_name='sl_channels')
    op.drop_index(op.f('ix_sl_channels_archived_at'), table_name='sl_channels')
    op.drop_table('sl_channels')
    # ### end Alembic commands ###