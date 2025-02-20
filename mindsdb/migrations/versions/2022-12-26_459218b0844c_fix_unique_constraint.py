"""fix_unique_constraint

Revision ID: 459218b0844c
Revises: d429095b570f
Create Date: 2022-12-26 13:40:57.141241

"""
from alembic import op

revision = '459218b0844c'
down_revision = 'd429095b570f'
branch_labels = None
depends_on = None


def upgrade():
    try:
        with op.batch_alter_table('project', schema=None) as batch_op:
            batch_op.drop_constraint('unique_integration_name_company_id', type_='unique')
            batch_op.create_unique_constraint('unique_project_name_company_id', ['name', 'company_id'])
    except Exception:
        pass


def downgrade():
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_constraint('unique_project_name_company_id', type_='unique')
        batch_op.create_unique_constraint('unique_integration_name_company_id', ['name', 'company_id'])
