from sqlalchemy import (
    MetaData, Table, Column, Integer, String
)

# naming_convention = {
#     'ix': 'ix_%(column_0_label)s',
#     'uq': 'uq_%(table_name)s_%(column_0_name)s',
#     'ck': 'ck_%(table_name)s_%(constraint_name)s',
#     'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
#     'pk': 'pk_%(table_name)s'
# }
#
# metadata = MetaData(naming_convention=naming_convention)

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('password', String, nullable=False),
)
