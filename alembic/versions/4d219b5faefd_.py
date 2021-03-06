"""empty message

Revision ID: 4d219b5faefd
Revises: a774918f4d02
Create Date: 2021-02-11 14:44:50.608093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d219b5faefd'
down_revision = 'a774918f4d02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sl_emojis',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=2048), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sl_emojis_url'), 'sl_emojis', ['url'], unique=False)
    op.create_table('sl_messages',
    sa.Column('id', sa.String(length=17), nullable=False),
    sa.Column('channel_id', sa.String(length=11), nullable=False),
    sa.Column('thread_id', sa.String(length=17), nullable=True),
    sa.Column('content', sa.UnicodeText(), nullable=True),
    sa.Column('user_id', sa.String(length=11), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['channel_id'], ['sl_channels.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['sl_users.id'], ),
    sa.PrimaryKeyConstraint('id', 'channel_id')
    )
    op.create_index(op.f('ix_sl_messages_deleted'), 'sl_messages', ['deleted'], unique=False)
    op.create_index(op.f('ix_sl_messages_thread_id'), 'sl_messages', ['thread_id'], unique=False)
    op.create_index(op.f('ix_sl_messages_user_id'), 'sl_messages', ['user_id'], unique=False)
    op.create_table('sl_files',
    sa.Column('message_id', sa.String(length=17), nullable=False),
    sa.Column('channel_id', sa.String(length=11), nullable=False),
    sa.Column('url', sa.String(length=2048), nullable=False),
    sa.ForeignKeyConstraint(['message_id', 'channel_id'], ['sl_messages.id', 'sl_messages.channel_id'], ),
    sa.PrimaryKeyConstraint('message_id', 'channel_id', 'url')
    )
    op.create_table('sl_reactions',
    sa.Column('message_id', sa.String(length=17), nullable=False),
    sa.Column('channel_id', sa.String(length=11), nullable=False),
    sa.Column('user_id', sa.String(length=11), nullable=False),
    sa.Column('emoji_id', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['message_id', 'channel_id'], ['sl_messages.id', 'sl_messages.channel_id'], ),
    sa.PrimaryKeyConstraint('message_id', 'channel_id', 'user_id', 'emoji_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sl_reactions')
    op.drop_table('sl_files')
    op.drop_index(op.f('ix_sl_messages_user_id'), table_name='sl_messages')
    op.drop_index(op.f('ix_sl_messages_thread_id'), table_name='sl_messages')
    op.drop_index(op.f('ix_sl_messages_deleted'), table_name='sl_messages')
    op.drop_table('sl_messages')
    op.drop_index(op.f('ix_sl_emojis_url'), table_name='sl_emojis')
    op.drop_table('sl_emojis')
    # ### end Alembic commands ###
